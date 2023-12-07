# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain nodes under a given node of the OPC-UA address space. 
# For each node, it displays its browse name and node ID.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Navigation.Parsing import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

browsePathParser = UABrowsePathParser('http://test.org/UA/Data/')
nodeDescriptor = UANodeDescriptor(browsePathParser.Parse('[ObjectsFolder]/Data/Static/UserScalar'))

# Instantiate the client object.
client = EasyUAClient()

# Perform the operation.
try:
    nodeElements = IEasyUAClientExtension.Browse(client,
         endpointDescriptor,
         nodeDescriptor,
         UABrowseParameters.AllForwardReferences)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElements:
    assert nodeElement is not None
    print(nodeElement.BrowseName, ': ', nodeElement.NodeId, sep='')

##endregion Example
