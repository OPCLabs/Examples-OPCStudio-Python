# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read value of server's NamespaceArray, and display the namespace URIs in it.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Perform the operation: Obtain value of a node.
try:
    value = IEasyUAClientExtension.ReadValue(client,
                                             endpointDescriptor,
                                             UANodeDescriptor(UAVariableIds.Server_NamespaceArray)) # i=2255
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

if not isinstance(value, Array):
    print('*** Not an array')
    exit()
arrayValue = value

# Display results.
for i, element in enumerate(arrayValue):
    print(i, ': ', element, sep='')

print()
print('Finished.')

##endregion Example
