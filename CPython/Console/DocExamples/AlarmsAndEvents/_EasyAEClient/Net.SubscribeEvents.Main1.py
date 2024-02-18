# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to events and display the event message with each notification. It also shows how
# to unsubscribe afterwards.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
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

print('Processing event notifications for 1 minute...')
time.sleep(60)

print('Unsubscribing events...')
client.UnsubscribeAllEvents()

client.Notification -= notification

print('Finished.')

##endregion Example
