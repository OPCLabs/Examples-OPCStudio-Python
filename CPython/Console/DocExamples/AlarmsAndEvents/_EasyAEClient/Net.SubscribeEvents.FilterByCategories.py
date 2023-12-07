# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to filter the events by their category.

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
    print()
    print(e)
    if not e.Succeeded:
        return
    print('Refresh: ', e.Refresh, sep='')
    print('RefreshComplete: ', e.RefreshComplete, sep='')
    eventData = e.EventData
    if eventData is not None:
        print('Event.CategoryId: ', eventData.CategoryId, sep='')
        print('Event.QualifiedSourceName: ', eventData.QualifiedSourceName, sep='')
        print('Event.Message: ', eventData.Message, sep='')
        print('Event.Active: ', eventData.Active, sep='')
        print('Event.Acknowledged: ', eventData.Acknowledged, sep='')


# Instantiate the OPC-A&E client object.
aeClient = EasyAEClient()

# Instantiate the OPC-DA client object.
daClient = EasyDAClient()

#
aeClient.Notification += notification

print('Processing event notifications...')
subscriptionFilter = AESubscriptionFilter()
subscriptionFilter.Categories = [15531778]
# You can also filter using event types, severity, areas, and sources.
handle = IEasyAEClientExtension.SubscribeEvents(aeClient, '', 'OPCLabs.KitEventServer.2', 1000, None, subscriptionFilter)

# Allow time for initial refresh.
time.sleep(5)

# Set some events to active state.
try:
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.Activate', True)
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState2.Activate', True)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

time.sleep(10)

aeClient.UnsubscribeEvents(handle)
aeClient.Notification -= notification

print('Finished.')

##endregion Example
