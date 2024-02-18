# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to write data (a value, timestamps and status code) into a single attribute of a node.
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

# Instantiate the client object
client = EasyUAClient()

print("Modifying data of a node's attribute...")
try:
    IEasyUAClientExtension.Write(client,
        endpointDescriptor,
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10221'),
        UAAttributeData(12345, UAStatusCode(UASeverity.GoodOrSuccess), DateTime.UtcNow))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
