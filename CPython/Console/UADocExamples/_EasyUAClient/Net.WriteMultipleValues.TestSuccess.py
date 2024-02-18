# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to write values into 3 nodes at once, test for success of each write and display the exception
# message in case of failure.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object
client = EasyUAClient()

print('Modifying values of nodes...')
writeResultArray = IEasyUAClientExtension.WriteMultipleValues(client, [
    UAWriteValueArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10221'), 23456),
    UAWriteValueArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10226'),
                          'This string cannot be converted to Double'),
    UAWriteValueArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;s=UnknownNode'), 'ABC'),
    ])

for i, writeResult in enumerate(writeResultArray):
    if writeResult.Succeeded:
        print('writeResultArray[', i, ']: success', sep='')
    else:
        print('writeResultArray[', i, '] *** Failure: ', writeResult.Exception.GetBaseException().Message, sep='')

print()
print('Finished.')

##endregion Example
