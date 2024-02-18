# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain all leaves under the "Simulation" branch of the address space. For each leaf, it
# displays the ItemID of the node.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Perform the operation.
try:
    nodeElements = IEasyDAClientExtension.BrowseLeaves(client, '', 'OPCLabs.KitServer.2', 'Simulation')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElements:
    print('NodeElements["', nodeElement.Name, '"].ItemId: ', nodeElement.ItemId, sep='')

##endregion Example
