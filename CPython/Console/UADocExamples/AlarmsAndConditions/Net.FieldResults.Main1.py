# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to display all fields of incoming events, or extract specific fields.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.AlarmsAndConditions import *
from OpcLabs.EasyOpc.UA.Filtering import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def eventNotification(sender, eventArgs):
    print()

    # Display the event.
    if eventArgs.EventData is None:
        print(eventArgs)
        return
    print('All fields:')
    for pair in eventArgs.EventData.FieldResults:
        attributeField = pair.Key
        valueResult = pair.Value
        print('  ', attributeField, ' -> ', valueResult, sep='')

    # Extracting a specific field using a standard operand symbol.
    print('Source name: ',
          eventArgs.EventData.FieldResults.get_Item(UAAttributeField(UABaseEventObject.Operands.SourceName)),
          sep='')

    # Extracting a specific field using an event type ID and a simple relative path.
    print('Message: ',
          eventArgs.EventData.FieldResults.get_Item(UAAttributeField(
              UAFilterElements.SimpleAttribute(UANodeDescriptor(UAObjectTypeIds.BaseEventType), '/Message'))),
          sep='')


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

print()
print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
