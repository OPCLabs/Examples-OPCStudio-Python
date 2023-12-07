# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to changes of multiple items and obtain the item changed events by pulling them.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Instantiate the client object
client = EasyDAClient()
# In order to use event pull, you must set a non-zero queue capacity upfront.
client.PullItemChangedQueueCapacity = 1000

print('Subscribing item changes...')
client.SubscribeMultipleItems([
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'UnknownItem', 1000, None),
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
