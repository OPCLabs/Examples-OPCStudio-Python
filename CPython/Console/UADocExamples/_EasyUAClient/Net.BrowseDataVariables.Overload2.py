# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain data variables under the "Server" node in the address space.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain data variables under "Server" node.
try:
    nodeElementCollection = IEasyUAClientExtension.BrowseDataVariables(client,
                                                                       endpointDescriptor,
                                                                       UANodeDescriptor(UAObjectIds.Server))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElementCollection:
    print()
    print('nodeElement.DisplayName: ', nodeElement.DisplayName, sep='')
    print('nodeElement.NodeId: ', nodeElement.NodeId, sep='')
    print('nodeElement.NodeId.ExpandedText: ', nodeElement.NodeId.ExpandedText, sep='')

print()
print('Finished.')

##endregion Example
