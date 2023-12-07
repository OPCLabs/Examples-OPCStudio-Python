# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read a Low state of a limit alarm. Note that you should not normally read a state of an alarm
# from inside its event notification, because the state might have already changed. Instead, include the information you
# need in the Select clauses when subscribing for the event.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.AlarmsAndConditions import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def eventNotification(sender, eventArgs):
    print()
    # Display the event.
    if eventArgs.EventData is None:
        print(eventArgs)
        return
    baseEventObject = eventArgs.EventData.BaseEvent
    print('Source name: ', baseEventObject.SourceName, sep='')
    print('Message: ', baseEventObject.Message, sep='')
    print('Severity: ', baseEventObject.Severity, sep='')


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')

# Instantiate the client object and hook events.
client = EasyUAClient()
client.EventNotification += eventNotification

print('Subscribing...')
IEasyUAClientExtension.SubscribeEvent(
    client,
    endpointDescriptor,
    UANodeDescriptor(UAObjectIds.Server),
    1000)

print('Processing event notifications for 30 seconds...')
time.sleep(30)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
