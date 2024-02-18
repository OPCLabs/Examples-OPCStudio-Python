# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to events and obtain the notification events by pulling them.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *


# Instantiate the client object
client = EasyAEClient()
# In order to use event pull, you must set a non-zero queue capacity upfront.
client.PullNotificationQueueCapacity = 1000

print('Subscribing events...')
handle = IEasyAEClientExtension.SubscribeEvents(client, '', 'OPCLabs.KitEventServer.2', 1000)

print('Processing event notifications for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    eventArgs = IEasyAEClientExtension.PullNotification(client, 2*1000)
    if eventArgs is not None:
        # Handle the notification event
        print(eventArgs)

print('Unsubscribing events...')
client.UnsubscribeAllEvents()

print('Finished.')

##endregion Example
