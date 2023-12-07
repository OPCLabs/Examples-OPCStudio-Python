# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to write a value into a single node.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Instantiate the client object.
client = EasyUAClient()

# Perform the operation.
try:
    IEasyUAClientExtension.WriteValue(client,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10221'),
        12345)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
