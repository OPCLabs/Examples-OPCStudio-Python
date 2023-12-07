# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to changes of multiple monitored items, pull events, and display each change.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Instantiate the client object
client = EasyUAClient()
# In order to use event pull, you must set a non-zero queue capacity upfront.
client.PullDataChangeNotificationQueueCapacity = 1000

print('Subscribing...')
client.SubscribeMultipleMonitoredItems([
    EasyUAMonitoredItemArguments(
        None,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10845'),
        UAMonitoringParameters(1000)),
    EasyUAMonitoredItemArguments(
        None,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
        UAMonitoringParameters(1000)),
    EasyUAMonitoredItemArguments(
        None,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10855'),
        UAMonitoringParameters(1000)),
    ])

print('Processing data change events for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    eventArgs = IEasyUAClientExtension.PullDataChangeNotification(client, 2*1000)
    if eventArgs is not None:
        # Handle the notification event
        print(eventArgs)

##endregion Example
