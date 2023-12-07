# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to events and display the event message with each notification, using a regular
# callback method.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *


# Notification callback.
def callback(sender, e):
    assert e is not None
    if not e.Succeeded:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')
        return
    else:
        if e.EventData is not None:
            print(e.EventData.Message)


# Instantiate the client object
client = EasyAEClient()

print('Subscribing events...')
# The callback is a regular method that  displays the event message.
handle = IEasyAEClientExtension.SubscribeEvents(client,
                                                '', 'OPCLabs.KitEventServer.2', 1000,
                                                EasyAENotificationEventHandler(callback))

print('Processing event notifications for 20 seconds...')
time.sleep(20)

print('Unsubscribing events...')
client.UnsubscribeAllEvents()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
