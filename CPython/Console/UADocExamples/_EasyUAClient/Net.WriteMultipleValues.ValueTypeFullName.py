# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to write values into 3 nodes at once, specifying a type's full name explicitly. It tests for
# success of each write and displays the exception message in case of failure.
#
# Reasons for specifying the type explicitly might be:
# - The data type in the server has subtypes, and the client therefore needs to pick the subtype to be written.
# - The data type that the reports is incorrect.
# - Writing with an explicitly specified type is more efficient.
#
# Alternative ways of specifying the type are using the ValueType or ValueTypeCode properties.
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
writeValueArguments1 = UAWriteValueArguments(endpointDescriptor,
                                             UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10221'), 23456)
writeValueArguments1.ValueTypeFullName = 'System.Int32' # here is the type explicitly specified
writeValueArguments2 = UAWriteValueArguments(endpointDescriptor,
                                             UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10226'),
                                             'This string cannot be converted to Double')
writeValueArguments2.ValueTypeFullName = 'System.Double' # here is the type explicitly specified
writeValueArguments3 = UAWriteValueArguments(endpointDescriptor,
                                             UANodeDescriptor('nsu=http://test.org/UA/Data/ ;s=UnknownNode'),
                                             'ABC')
writeValueArguments3.ValueTypeFullName = 'System.String' # here is the type explicitly specified

writeResultArray = IEasyUAClientExtension.WriteMultipleValues(client,
    [writeValueArguments1, writeValueArguments2, writeValueArguments3])

for i, writeResult in enumerate(writeResultArray):
    if writeResult.Succeeded:
        print('writeResultArray[', i, ']: success', sep='')
    else:
        print('writeResultArray[', i, '] *** Failure: ', writeResult.Exception.GetBaseException().Message, sep='')

print()
print('Finished.')

##endregion Example
