# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read data (value, timestamps, and status code) of 3 attributes at once. In this example,
# we are reading a Value attribute of 3 different nodes, but the method can also be used to read multiple attributes
# of the same node.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
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
attributeDataResultArray = client.ReadMultiple([
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10845')),
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853')),
    UAReadArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10855')),
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
