# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read a value from a single node that is an array of UInt16.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Instantiate the client object.
client = EasyUAClient()

print('Obtaining value of a node...')
try:
    # UInt16 is returned as Int32, because UInt16 is not a CLS-compliant type (and is not supported in VB.NET).
    value = IEasyUAClientExtension.ReadValue(client,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;ns=2;i=10932')) # /Data.Dynamic.Array.UInt16Value
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
if value is not None:
    print(value[0])
    print(value[1])
    print(value[2])

print()
print('Finished.')

##endregion Example
