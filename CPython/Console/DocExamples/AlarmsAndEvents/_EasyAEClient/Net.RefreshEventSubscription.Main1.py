# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to for a refresh for all active conditions and inactive, unacknowledged conditions.
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
    AENodeDescriptor('Simulation.ConditionState2'),
    AENodeDescriptor('Simulation.ConditionState3'),
]
handle = IEasyAEClientExtension.SubscribeEvents(aeClient, '', 'OPCLabs.KitEventServer.2', 1000, None, subscriptionFilter)

# The component will perform auto-refresh at this point, give it time to happen.
print('Waiting for 10 seconds...')
time.sleep(10)

# Set some events to active state, which will cause them to appear in refresh.
print('Activating conditions and waiting for 10 seconds...')
try:
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.Activate', True)
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState2.Activate', True)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()
time.sleep(10)

print('Refreshing event subscription and waiting for 10 seconds...')
aeClient.RefreshEventSubscription(handle)
time.sleep(10)

aeClient.UnsubscribeEvents(handle)
aeClient.Notification -= notification

print('Finished.')

##endregion Example
