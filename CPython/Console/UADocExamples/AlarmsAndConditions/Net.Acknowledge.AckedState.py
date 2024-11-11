# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain acknowledged state of events, and acknowledge an event that is not acknowledged yet.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from System.Threading import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.AlarmsAndConditions import *
from OpcLabs.EasyOpc.UA.Filtering import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def eventNotification(sender, eventArgs):
    global ackedStateIdOperand
    global anEvent
    global eventId
    global nodeId

    if not eventArgs.Succeeded:
        print('*** Failure: ', eventArgs.ErrorMessageBrief, sep='')
        return

    eventData = eventArgs.EventData
    if not eventData is None:
        baseEventObject = eventData.BaseEvent
        print(baseEventObject)

        # Obtain the acknowledge state of the event.
        ackedStateIdResult = eventData.FieldResults.get_Item(UAAttributeField(ackedStateIdOperand))
        assert ackedStateIdResult is not None
        if not ackedStateIdResult.Succeeded:
            return
        ackedStateId = ackedStateIdResult.Value
        print('AckedState/Id: ', ackedStateId, sep='')

        # Only attempt to acknowledge when not acknowledged yet.
        if ackedStateId != False:
            return

        # Make sure we do not catch the event more than once.
        if anEvent.WaitOne(0):
            return

        nodeId = baseEventObject.NodeId
        eventId = baseEventObject.EventId

        anEvent.Set()


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')

# Instantiate the client objects.
client = EasyUAClient()
alarmsAndConditionsClient = IEasyUAClientExtension.AsAlarmsAndConditionsClient(client)

nodeId = None
eventId = None
anEvent = ManualResetEvent(False)   # initialState

# Prepare the Select clauses.
selectClauses = UABaseEventObject.AllFields
ackedStateIdOperand = UAFilterElements.SimpleAttribute(
    UANodeDescriptor(UAObjectTypeIds.BaseEventType),
    '/AckedState/Id')
selectClauses.Add(UAAttributeField(ackedStateIdOperand))

print('Subscribing...')
eventFilterBuilder = UAEventFilterBuilder(
    # We will auto-acknowledge an event with severity less than 200.
    UAFilterElements.LessThan(UABaseEventObject.Operands.Severity, 200),
    selectClauses)
IEasyUAClientExtension.SubscribeEvent(
    client,
    endpointDescriptor,
    UANodeDescriptor(UAObjectIds.Server),
    1000,
    UAEventFilterBuilder.ToUAEventFilter(eventFilterBuilder),
    EasyUAEventNotificationEventHandler(eventNotification),
    None)   # state

print('Waiting for an acknowledgeable event for 10 minutes...')
if not anEvent.WaitOne(10*60*1000):
    print('Event not received.')
    exit()

print()
print('Acknowledging an event...')
try:
    alarmsAndConditionsClient.Acknowledge(
        endpointDescriptor,
        UANodeDescriptor(nodeId),
        eventId,
        'Acknowledged by an automated example code.')
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
print('Event successfully acknowledged.')

print()
print('Waiting for 5 seconds...')
time.sleep(5)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
