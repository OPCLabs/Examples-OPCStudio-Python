# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to create and use two isolated client objects, resulting in two separate connections to the
# target OPC UA server.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# The callback is a regular method the displays the value.
def dataChangeCallback(sender, eventArgs):
    print('[', eventArgs.Arguments.State, '] ', sep='', end='')
    if eventArgs.Succeeded:
        assert eventArgs.AttributeData is not None
        print('Value: ', eventArgs.AttributeData.Value, sep='')
    else:
        print('*** Failure: ', eventArgs.ErrorMessageBrief, sep='')


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client objects and make them isolated.
client1 = EasyUAClient()
client1.Isolated = True
client2 = EasyUAClient()
client2.Isolated = True

print('Subscribing...')
IEasyUAClientExtension.SubscribeDataChange(client1,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
    1000,
    EasyUADataChangeNotificationEventHandler(dataChangeCallback),
    1)  # state
IEasyUAClientExtension.SubscribeDataChange(client2,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
    1000,
    EasyUADataChangeNotificationEventHandler(dataChangeCallback),
    2)  # state

print('Processing data change events for 10 seconds...')
time.sleep(10)

print('Unsubscribing...')
client1.UnsubscribeAllMonitoredItems()
client2.UnsubscribeAllMonitoredItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
