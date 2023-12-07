# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to unsubscribe from specific event notifications.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *


# Notification event handler
def notification(sender, e):
    if not e.Succeeded:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')
        return
    else:
        if e.EventData is not None:
            print(e.EventData.Message)


# Instantiate the client object
client = EasyAEClient()

client.Notification += notification

print('Subscribing events...')
handle = IEasyAEClientExtension.SubscribeEvents(client, '', 'OPCLabs.KitEventServer.2', 1000)

print('Waiting for 10 seconds...')
time.sleep(10)

print('Unsubscribing events...')
client.UnsubscribeEvents(handle)

print('Waiting for 10 seconds...')
time.sleep(10)

client.Notification -= notification

print('Finished.')

##endregion Example
