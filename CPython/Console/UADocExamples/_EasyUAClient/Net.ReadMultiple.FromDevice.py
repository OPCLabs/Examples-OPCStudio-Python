# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read data value of 3 nodes at once, from the device (data source).
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain attribute data. By default, the Value attributes of the nodes will be read.
# The parameters specify reading from the device (data source), which may be slow but provides the very latest
# data.
attributeDataResultArray = client.ReadMultiple([
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10845'),
                    UAReadParameters.FromDevice),
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
                    UAReadParameters.FromDevice),
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10855'),
                    UAReadParameters.FromDevice),
    ])

# Display results.
for attributeDataResult in attributeDataResultArray:
    if attributeDataResult.Succeeded:
        print('AttributeData: ', attributeDataResult.AttributeData, sep='')
    else:
        print('*** Failure: ', attributeDataResult.ErrorMessageBrief, sep='')

print()
print('Finished.')

##endregion Example
