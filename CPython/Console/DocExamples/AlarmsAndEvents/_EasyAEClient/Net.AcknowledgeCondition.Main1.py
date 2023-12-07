# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to acknowledge an event condition in the OPC server.

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
    global aeClient
    global done

    if not e.Succeeded:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')
        return
    print('Refresh: ', e.Refresh, sep='')
    print('RefreshComplete: ', e.RefreshComplete, sep='')
    eventData = e.EventData
    if eventData is not None:
        print('EventData.QualifiedSourceName: ', eventData.QualifiedSourceName, sep='')
        print('EventData.Message: ', eventData.Message, sep='')
        print('EventData.Active: ', eventData.Active, sep='')
        print('EventData.ActiveTime: ', eventData.ActiveTime, sep='')
        print('EventData.ActiveTimeTicks: ', eventData.ActiveTimeTicks, sep='')
        print('EventData.Acknowledged: ', eventData.Acknowledged, sep='')
        print('EventData.AcknowledgeRequired: ', eventData.AcknowledgeRequired, sep='')
        print('EventData.Cookie: ', eventData.Cookie, sep='')
        if eventData.AcknowledgeRequired:
            print('>>>>> ACKNOWLEDGING THIS EVENT')
            try:
                IEasyAEClientExtension.AcknowledgeCondition(aeClient,
                                                            '', 'OPCLabs.KitEventServer.2',
                                                            'Simulation.ConditionState1', 'Simulated',
                                                            eventData.ActiveTimeTicks, eventData.Cookie,
                                                            'Myself')  # acknowledgerId
                # The precise ActiveTime is important for event acknowledgement in OPC A&E. Python.NET, however,
                # represents .NET DateTime to Python 'datetime' object, possibly losing precision. For this reason,
                # use AEEventData.ActiveTimeTicks (as above), and not AEEventData.ActiveTime.
                # aeClient.AcknowledgeCondition('', 'OPCLabs.KitEventServer.2',
                #                               'Simulation.ConditionState1', 'Simulated',
                #                               eventData.ActiveTime, eventData.Cookie)
            except OpcException as opcException:
                print('*** Failure: ' + opcException.GetBaseException().Message)
                done = True
                return
            print('>>>>> EVENT ACKNOWLEDGED')
            done = True


# Instantiate the OPC-A&E client object.
aeClient = EasyAEClient()

# Instantiate the OPC-DA client object.
daClient = EasyDAClient()

#
aeClient.Notification += notification

print('Processing event notifications for 1 minute...')
subscriptionFilter = AESubscriptionFilter()
subscriptionFilter.Sources = [AENodeDescriptor('Simulation.ConditionState1')]
handle = IEasyAEClientExtension.SubscribeEvents(aeClient, '', 'OPCLabs.KitEventServer.2', 1000, None,
                                                subscriptionFilter)

# Give the refresh operation time to complete.
time.sleep(5)

# Trigger an acknowledgeable event.
done = False
try:
    IEasyDAClientExtension.WriteItemValue(daClient, '', 'OPCLabs.KitServer.2',
                                          'SimulateEvents.ConditionState1.Activate', True)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

endTime = time.time() + 60
while (not done) and (time.time() < endTime):
    time.sleep(1)

# Give some time to also receive the acknowledgement notification.
time.sleep(5)

aeClient.UnsubscribeAllEvents()
aeClient.Notification -= notification

print('Finished.')

##endregion Example
