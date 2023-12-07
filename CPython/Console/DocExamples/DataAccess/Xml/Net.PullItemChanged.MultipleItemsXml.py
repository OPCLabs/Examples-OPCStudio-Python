# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to changes of multiple OPC XML-DA items and obtain the item changed events by pulling them.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Instantiate the client object
client = EasyDAClient()
# In order to use event pull, you must set a non-zero queue capacity upfront.
client.PullItemChangedQueueCapacity = 1000

print('Subscribing item changes...')

itemSubscriptionArguments1 = EasyDAItemSubscriptionArguments(
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    DAItemDescriptor('Dynamic/Analog Types/Double'),
    DAGroupParameters(1000),
    None)

itemSubscriptionArguments2 = EasyDAItemSubscriptionArguments(
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    DAItemDescriptor('Dynamic/Analog Types/Double[]'),
    DAGroupParameters(1000),
    None)

itemSubscriptionArguments3 = EasyDAItemSubscriptionArguments(
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    DAItemDescriptor('Dynamic/Analog Types/Int'),
    DAGroupParameters(1000),
    None)

# Intentionally specifying an unknown item here, to demonstrate its behavior.
itemSubscriptionArguments4 = EasyDAItemSubscriptionArguments(
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    DAItemDescriptor('SomeUnknownItem'),
    DAGroupParameters(1000),
    None)

client.SubscribeMultipleItems([
    itemSubscriptionArguments1,
    itemSubscriptionArguments2,
    itemSubscriptionArguments3,
    itemSubscriptionArguments4,
    ])

print('Processing item changes for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    eventArgs = IEasyDAClientExtension.PullItemChanged(client, 2*1000)
    if eventArgs is not None:
        # Handle the notification event
        if (eventArgs.Succeeded):
            print(eventArgs.Arguments.ItemDescriptor.ItemId, ': ', eventArgs.Vtq, sep='')
        else:
            print(eventArgs.Arguments.ItemDescriptor.ItemId, ' *** Failure: ', eventArgs.ErrorMessageBrief, sep='')

print('Unsubscribing item changes...')
client.UnsubscribeAllItems()

print('Finished.')

##endregion Example
