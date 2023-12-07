# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to call a single method, and pass arguments to and from it.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# 
inputs = [False, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
typeCodes = [
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

# Instantiate the client object.
client = EasyUAClient()

# Perform the operation.
try:
    outputs = IEasyUAClientExtension.CallMethod(client,
        endpointDescriptor,
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10755'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10756'),
        inputs,
        typeCodes)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for i, value in enumerate(outputs):
     print('outputs[', i, ']: ', value, sep='')


# Example output:
#outputs[0]: False
#outputs[1]: 1
#outputs[2]: 2
#outputs[3]: 3
#outputs[4]: 4
#outputs[5]: 5
#outputs[6]: 6
#outputs[7]: 7
#outputs[8]: 8
#outputs[9]: 9.0
#outputs[10]: 10.0

##endregion Example
