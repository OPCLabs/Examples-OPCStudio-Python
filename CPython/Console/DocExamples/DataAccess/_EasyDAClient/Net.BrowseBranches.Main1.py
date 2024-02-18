# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain all branches at the root of the address space. For each branch, it displays whether
# it may have child nodes.
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
    nodeElements = IEasyDAClientExtension.BrowseBranches(client, '', 'OPCLabs.KitServer.2', '')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElements:
    print('NodeElements["', nodeElement.Name, '"].HasChildren: ', nodeElement.HasChildren, sep='')

##endregion Example
