# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read the Value attributes of 3 different nodes at once. Using the same method, it is also
# possible to read multiple attributes of the same node.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain values. By default, the Value attributes of the nodes will be read.
valueResultArray = IEasyUAClientExtension.ReadMultipleValues(client, [
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10845'),
                    UAAttributeId.DataType),
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
                    UAAttributeId.DataType),
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10855'),
                    UAAttributeId.DataType),
    ])

# Display results.
for valueResult in valueResultArray:
    print()
    #
    if valueResult.Succeeded:
        print('Value: ', valueResult.Value, sep='')
        if isinstance(valueResult.Value, UANodeId):
            dataTypeId = valueResult.Value
            print('dataTypeId.ExpandedText: ', dataTypeId.ExpandedText, sep='')
            print('dataTypeId.NamespaceUriString: ', dataTypeId.NamespaceUriString, sep='')
            print('dataTypeId.NamespaceIndex: ', dataTypeId.NamespaceIndex, sep='')
            print('dataTypeId.NumericIdentifier: ', dataTypeId.NumericIdentifier, sep='')
    else:
        print('*** Failure: ', valueResult.ErrorMessageBrief, sep='')

print()
print('Finished.')

##endregion Example
