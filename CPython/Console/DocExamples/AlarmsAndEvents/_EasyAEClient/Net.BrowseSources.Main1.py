# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain all sources under the "Simulation" area.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyAEClient()

# Perform the operation
try:
    nodeElements = IEasyAEClientExtension.BrowseSources(client, '', 'OPCLabs.KitEventServer.2', 'Simulation')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
for nodeElement in nodeElements:
    assert nodeElement is not None
    print('NodeElements["', nodeElement.Name, '"]:', sep='')
    print('    .QualifiedName: ', nodeElement.QualifiedName, sep='')

##endregion Example
