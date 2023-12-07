# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain all nodes under the "Simulation" branch of the address space. For each node, it displays
# whether the node is a branch or a leaf.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyDAClient()

# Perform the operation
try:
    nodeElements = IEasyDAClientExtension.BrowseNodes(client,
        '', 'OPCLabs.KitServer.2', 'Greenhouse', DABrowseParameters.Default)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
for nodeElement in nodeElements:
    print('NodeElements("' + nodeElement.Name + '"):')
    print('    .IsBranch:', nodeElement.IsBranch)
    print('    .IsLeaf:', nodeElement.IsLeaf)


# Example output:
#
#NodeElements("Register_ArrayOfI1"):
#    .IsBranch: False
#    .IsLeaf: True
#NodeElements("Register_ArrayOfI2"):
#    .IsBranch: False
#    .IsLeaf: True
#NodeElements("Register_ArrayOfI4"):
#    .IsBranch: False
#    .IsLeaf: True
#NodeElements("Staircase 0:2 (10 s)"):
#    .IsBranch: False
#    .IsLeaf: True
#NodeElements("Constant_VARIANT"):
#    .IsBranch: False
#    .IsLeaf: True
#...

##endregion Example
