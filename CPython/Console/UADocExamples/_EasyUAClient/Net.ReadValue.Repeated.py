# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to repeatedly read value of a single node, and display it.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
from datetime import datetime
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'
nodeIdExpandedText = 'nsu=http://test.org/UA/Data/ ;i=10221'
# Example settings with Softing dataFEED OPC Suite:
# 'endpointDescriptorUrlString = "'opc.tcp://localhost:4980/Softing_dataFEED_OPC_Suite_Configuration1'
# 'nsu=Local%20Items ;s=Local Items.EAK_Test1.EAK_Testwert1_I4'

# Instantiate the client object.
client = EasyUAClient()

for i in range(1, 61):
    print('@', datetime.now(), ': ', sep='', end='')

    # Obtain value of a node.
    try:
        value = IEasyUAClientExtension.ReadValue(client, endpointDescriptor, UANodeDescriptor(nodeIdExpandedText))
    except UAException as uaException:
        print('*** Failure: ' + uaException.GetBaseException().Message)
        exit()

    # Display results.
    print('Read ', value, sep='')

    time.sleep(1)

print()
print('Finished.')

##endregion Example
