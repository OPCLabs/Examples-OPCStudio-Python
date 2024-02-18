# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Recursively browses and displays the nodes in the OPC address space, and attempts to read and display values of all
# OPC items it finds.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *

SERVER_CLASS = 'OPCLabs.KitServer.2'


def browseAndReadFromNode(parentItemId):
    global client
    #
    # Obtain all node elements under parentItemId.
    browseParameters = DABrowseParameters()  # no filtering whatsoever
    nodeElementCollection = client.BrowseNodes(ServerDescriptor(SERVER_CLASS),
                                               DANodeDescriptor(parentItemId),
                                               browseParameters)
    # BrowseNodes(...) may also throw OpcException; here it is handled by the caller.
    #
    for nodeElement in nodeElementCollection:
        assert nodeElement is not None
        print(nodeElement)

        # If the node is a leaf, it might be possible to read from it.
        if nodeElement.IsLeaf:
            # Determine what to display - either the value read, or exception message in case of failure.
            try:
                value = IEasyDAClientExtension.ReadItemValue(client, '', SERVER_CLASS, nodeElement.ItemId)
                display = value
            except OpcException as opcException:
                display = '** ' + opcException.GetBaseException().Message + ' **'
            #
            print(nodeElement.ItemId, ' -> ', display, sep='')
        # If the node is not a leaf, just display its itemId.
        else:
            print(nodeElement.ItemId)

        # If the node is a branch, browse recursively into it.
        if nodeElement.IsBranch and nodeElement.ItemId != 'SimulateEvents':
            # this branch is too big for the purpose of this example
            browseAndReadFromNode(nodeElement.ItemId)


# Instantiate the client object.
client = EasyDAClient('Browsing and reading values...')

print('Browsing and reading values...')

# Do the actual browsing and reading, starting from root of OPC address space (denoted by empty string for itemId).
try:
    browseAndReadFromNode('')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
