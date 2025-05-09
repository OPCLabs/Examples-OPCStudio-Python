# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to set the filtering criteria to be used for the event subscription.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
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
    print('Refresh: ', e.Refresh, sep='')
    print('RefreshComplete: ', e.RefreshComplete, sep='')
    eventData = e.EventData
    if eventData is not None:
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
subscriptionFilter.Sources = [
    AENodeDescriptor('Simulation.ConditionState1'),
    AENodeDescriptor('Simulation.ConditionState3'),
]
# You can also filter using event types, categories, severity, and areas.
handle = IEasyAEClientExtension.SubscribeEvents(aeClient, '', 'OPCLabs.KitEventServer.2', 1000, None, subscriptionFilter)

# Allow time for initial refresh
time.sleep(5)

# Set some events to active state.
try:
    # The activation below will come from a source contained in a filter and the notification will arrive.
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2', 'SimulateEvents.ConditionState1.Activate', True)
    # The activation below will come from a source that is not contained in a filter and the notification will not
    # arrive.
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2', 'SimulateEvents.ConditionState2.Activate', True)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

time.sleep(10)

aeClient.UnsubscribeAllEvents()
aeClient.Notification -= notification

print('Finished.')

##endregion Example
