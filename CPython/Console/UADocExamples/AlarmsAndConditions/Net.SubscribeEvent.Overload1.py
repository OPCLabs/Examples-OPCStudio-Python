# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to event notifications and display each incoming event.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
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
