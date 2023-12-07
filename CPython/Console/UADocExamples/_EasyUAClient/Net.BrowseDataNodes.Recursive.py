# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain "data nodes" under the "Objects" node, recursively.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def browseFromNode(client, endpointDescriptor, parentNodeDescriptor, level):
    assert client is not None
    assert endpointDescriptor is not None
    assert parentNodeDescriptor is not None

    # Obtain all node elements under parentNodeDescriptor
    nodeElementCollection = IEasyUAClientExtension.BrowseDataNodes(client, endpointDescriptor, parentNodeDescriptor)
    # Remark: BrowseDataNodes(...) may throw UAException; we handle it in the calling method.
    #
    for nodeElement in nodeElementCollection:
        assert nodeElement is not None

        print(' '*(level*2), end='')    # indent
        print(nodeElement)

        # Browse recursively into the node.
        # The UANodeElement has an implicit conversion to UANodeDescriptor.
        browseFromNode(client, endpointDescriptor, nodeElement.ToUANodeDescriptor(), level + 1)

        # Note that the number of nodes you obtain through recursive browsing may be very large, or even infinite.
        # Production code should contain appropriate safeguards for these cases.


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

try:
    browseFromNode(client, endpointDescriptor, UANodeDescriptor(UAObjectIds.ObjectsFolder), 0)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
