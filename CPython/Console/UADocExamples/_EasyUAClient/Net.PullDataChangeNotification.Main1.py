# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to changes of a single monitored item, pull events, and display each change.

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
IEasyUAClientExtension.SubscribeDataChange(client,
    UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
    1000)

print('Processing data change events for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    eventArgs = IEasyUAClientExtension.PullDataChangeNotification(client, 2*1000)
    if eventArgs is not None:
        # Handle the notification event
        print(eventArgs)

##endregion Example
