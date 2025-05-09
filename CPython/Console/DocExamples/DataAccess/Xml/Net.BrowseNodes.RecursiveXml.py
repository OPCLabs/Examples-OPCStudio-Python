# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to recursively browse the nodes in the OPC XML-DA address space.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import timeit

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


def browseFromNode(client, serverDescriptor, parentNodeDescriptor):
    global branchCount
    global leafCount

    assert client is not None
    assert serverDescriptor is not None
    assert parentNodeDescriptor is not None

    # Obtain all node elements under parentNodeDescriptor.
    browseParameters = DABrowseParameters() # no filtering whatsoever
    nodeElementCollection = client.BrowseNodes(serverDescriptor, parentNodeDescriptor, browseParameters)
    # BrowseNodes(...) may also throw OpcException; here it is handled by the caller.

    for nodeElement in nodeElementCollection:
        assert nodeElement is not None
        print(nodeElement)

        # If the node is a branch, browse recursively into it.
        if nodeElement.IsBranch:
            branchCount = branchCount + 1
            browseFromNode(client, serverDescriptor, DANodeDescriptor(nodeElement))
        else:
            leafCount = leafCount + 1


beginTime = timeit.default_timer()

# Instantiate the client object.
client = EasyDAClient()
branchCount = 0
leafCount = 0

try:
    browseFromNode(client,
                   ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
                   DANodeDescriptor(''))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

endTime = timeit.default_timer()
print()
print('Browsing has taken (milliseconds): ',(endTime - beginTime)*1000)
print('Branch count: ', branchCount);
print('Leaf count: ', leafCount);

##endregion Example
