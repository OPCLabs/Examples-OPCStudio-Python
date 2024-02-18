# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to call multiple methods, and pass arguments to and
# from them.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'
nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10755')

#
inputs1 = [False, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
typeCodes1 = [
    TypeCode.Boolean,
    TypeCode.SByte,
    TypeCode.Byte,
    TypeCode.Int16,
    TypeCode.UInt16,
    TypeCode.Int32,
    TypeCode.UInt32,
    TypeCode.Int64,
    TypeCode.UInt64,
    TypeCode.Single,
    TypeCode.Double,
    ]

inputs2 = [False, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'eleven']
typeCodes2 = [
    TypeCode.Boolean,
    TypeCode.SByte,
    TypeCode.Byte,
    TypeCode.Int16,
    TypeCode.UInt16,
    TypeCode.Int32,
    TypeCode.UInt32,
    TypeCode.Int64,
    TypeCode.UInt64,
    TypeCode.Single,
    TypeCode.Double,
    TypeCode.String,
    ]

# Instantiate the client object.
client = EasyUAClient()

# Perform the operation.
try:
    valueArrayResultArray = client.CallMultipleMethods([
        UACallArguments(endpointDescriptor, nodeDescriptor,
                        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10756'), inputs1, typeCodes1),
        UACallArguments(endpointDescriptor, nodeDescriptor,
                        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10774'), inputs2, typeCodes2),
        ])
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for i, valueArrayResult in enumerate(valueArrayResultArray):
    print()
    print('valueArrayResultArray[', i, ']:', sep='')
    if valueArrayResult.Succeeded:
        assert valueArrayResult.ValueArray is not None
        for j, outputValueArray in enumerate(valueArrayResult.ValueArray):
            print('    valueArray[', j, ']: ', outputValueArray, sep='')
    else:
        print('*** Failure: ', valueArrayResult.ErrorMessageBrief, sep='')

print()
print('Finished.')

##endregion Example
