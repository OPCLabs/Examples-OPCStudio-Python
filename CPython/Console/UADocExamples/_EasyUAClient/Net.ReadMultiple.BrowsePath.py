# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read the attributes of 4 OPC-UA nodes specified by browse paths at once, and display the
# results.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Navigation.Parsing import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Instantiate the browse path parser.
browsePathParser = UABrowsePathParser()
browsePathParser.DefaultNamespaceUriString = 'http://test.org/UA/Data/'

# Prepare arguments.
# Note: Add error handling around the following statement if the browse paths are not guaranteed to be
# syntactically valid.
readArgumentsArray = [
    UAReadArguments(endpointDescriptor,
                    UANodeDescriptor(browsePathParser.Parse('[ObjectsFolder]/Data/Dynamic/Scalar/FloatValue'))),
    UAReadArguments(endpointDescriptor,
                    UANodeDescriptor(browsePathParser.Parse('[ObjectsFolder]/Data/Dynamic/Scalar/SByteValue'))),
    UAReadArguments(endpointDescriptor,
                    UANodeDescriptor(browsePathParser.Parse('[ObjectsFolder]/Data/Static/Array/UInt16Value'))),
    UAReadArguments(endpointDescriptor,
                    UANodeDescriptor(browsePathParser.Parse('[ObjectsFolder]/Data/Static/UserScalar/Int32Value'))),
    ]

# Obtain attribute data.
attributeDataResultArray = client.ReadMultiple(readArgumentsArray)

# Display results.
for i, attributeDataResult in enumerate(attributeDataResultArray):
    if attributeDataResult.Succeeded:
        print('results[', i, '].AttributeData: ', attributeDataResult.AttributeData, sep='')
    else:
        print('results[', i, '] *** Failure: ', attributeDataResult.ErrorMessageBrief, sep='')

print()
print('Finished.')

##endregion Example
