# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
#  This example shows how to subscribe to event notifications, pull events, and display each incoming event.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')

# Instantiate the client object.
# In order to use event pull, you must set a non-zero queue capacity upfront.
client = EasyUAClient()
client.PullEventNotificationQueueCapacity = 1000

print('Subscribing...')
IEasyUAClientExtension.SubscribeEvent(
    client,
    endpointDescriptor,
    UANodeDescriptor(UAObjectIds.Server),
    1000)

print('Processing event notifications for 30 seconds...')
endTime = time.time() + 30
while time.time() < endTime:
    eventArgs = IEasyUAClientExtension.PullEventNotification(client, 2*1000)
    if eventArgs is not None:
        # Handle the notification event.
        print(eventArgs)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Finished.')

##endregion Example
