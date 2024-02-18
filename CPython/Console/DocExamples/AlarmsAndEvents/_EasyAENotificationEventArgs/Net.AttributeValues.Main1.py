# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to events with specified event attributes, and obtain the attribute values in
# event notifications.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Notification event handler
def notification(sender, e):
    if not e.Succeeded:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')
        return
    if (not e.Refresh) and (e.EventData is not None):
        # Display all received event attribute IDs and their corresponding values.
        print('Event attribute count: ', e.EventData.AttributeValues.Count, sep='')
        for pair in e.EventData.AttributeValues:
            print('    ', pair.Key, ': ', pair.Value, sep='')


# Instantiate the OPC-A&E client object.
aeClient = EasyAEClient()

# Instantiate the OPC-DA client object.
daClient = EasyDAClient()

#
aeClient.Notification += notification

# Inactivate the event condition (we will later activate it and receive the notification).
try:
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.Inactivate', True)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

subscriptionFilter = AESubscriptionFilter()
subscriptionFilter.Sources = [AENodeDescriptor('Simulation.ConditionState1')]

# Prepare a dictionary holding requested event attributes for each event category.
# The event category IDs and event attribute IDs are hard-coded here, but can be obtained from the OPC
# server by querying as well.
returnedAttributesByCategory = AEAttributeSetDictionary()
returnedAttributesByCategory.Add(0x00ECFF02, [0x00EB0003, 0x00EB0008])

print('Subscribing to events...')
handle = IEasyAEClientExtension.SubscribeEvents(aeClient, '', 'OPCLabs.KitEventServer.2', 1000, None,
                                                subscriptionFilter, returnedAttributesByCategory)

# Give the refresh operation time to complete.
time.sleep(5)

# Trigger an event carrying specified attributes (activate the condition).
try:
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.AttributeValues.15400963', 123456)
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.AttributeValues.15400968', 'Some string value')
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.Activate', True)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('Processing event notifications for 10 seconds...')
time.sleep(10)

aeClient.UnsubscribeEvents(handle)
aeClient.Notification -= notification

print('Finished.')

##endregion Example
