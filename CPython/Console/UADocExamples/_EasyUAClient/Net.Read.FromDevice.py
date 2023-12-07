# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read data from the device (data source) and display a value, timestamps, and status code.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Instantiate the client object.
client = EasyUAClient()

# Obtain attribute data. By default, the Value attribute of a node will be read.
# The parameters specify reading from the device (data source), which may be slow but provides the very latest
# data.
try:
    attributeData = IEasyUAClientExtension.Read(client,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
        UAReadParameters.FromDevice)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('Value: ', attributeData.Value)
print('ServerTimestamp: ', attributeData.ServerTimestamp)
print('SourceTimestamp: ', attributeData.SourceTimestamp)
print('StatusCode: ', attributeData.StatusCode)

##endregion Example
