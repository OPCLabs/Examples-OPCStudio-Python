# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to set fairly short OPC UA timeouts (failures can thus occur).

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def dataChangeNotification(sender, eventArgs):
    # Display value.
    if eventArgs.Succeeded:
        print('Value: ', eventArgs.AttributeData.Value, sep='')
    else:
        print('*** Failure: ', eventArgs.ErrorMessageBrief, sep='')


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object and set timeouts.
client = EasyUAClient()
client.Isolated = True
client.IsolatedParameters.SessionParameters.EndpointSelectionTimeout = 1500
client.IsolatedParameters.SessionParameters.SessionConnectTimeout = 3000
client.IsolatedParameters.SessionParameters.SessionTimeout = 3000
client.IsolatedParameters.SessionParameters.SessionTimeoutDebug = 3000

print('Subscribing...')
IEasyUAClientExtension.SubscribeDataChange(client,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
    1000,
    EasyUADataChangeNotificationEventHandler(dataChangeNotification))

print('Processing data change events for 10 seconds...')
time.sleep(10)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
