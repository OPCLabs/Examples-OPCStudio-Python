# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read a range of values from an array.
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

# Instantiate the client object.
client = EasyUAClient()

# Obtain the value, indicating that just the elements 2 to 4 should be returned
try:
    arrayValue = IEasyUAClientExtension.ReadValue(client,
                                                  endpointDescriptor,
                                                  UANodeDescriptor('nsu=http://test.org/UA/Data/ ;ns=2;i=10305'),    # /Data.Static.Array.Int32Value
                                                  UAIndexRangeList.OneDimension(2, 4))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for i, elementValue in enumerate(arrayValue):
    print('arrayValue[', i, ']: ', elementValue, sep='')

print()
print('Finished.')

##endregion Example
