# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to specify criteria for event notifications.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.AlarmsAndConditions import *
from OpcLabs.EasyOpc.UA.Filtering import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def eventNotification(sender, eventArgs):
    # Display the event.
    print(eventArgs)


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')

# Instantiate the client object and hook events.
client = EasyUAClient()
client.EventNotification += eventNotification

print('Subscribing...')

eventFilterBuilder = UAEventFilterBuilder(
    # Either the severity is >= 500, or the event comes from a specified source node.
    UAFilterElements.Or(
        UAFilterElements.GreaterThanOrEqual(UABaseEventObject.Operands.Severity, 500),
        UAFilterElements.Equals(
            UABaseEventObject.Operands.SourceNode,
            UANodeId('nsu=http://opcfoundation.org/Quickstarts/AlarmCondition ;ns=2;s=1:Metals/SouthMotor'))),
    UABaseEventObject.AllFields)

IEasyUAClientExtension.SubscribeEvent(
    client,
    endpointDescriptor,
    UANodeDescriptor(UAObjectIds.Server),
    1000,
    UAEventFilterBuilder.ToUAEventFilter(eventFilterBuilder))

print('Processing event notifications for 30 seconds...')
time.sleep(30)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
