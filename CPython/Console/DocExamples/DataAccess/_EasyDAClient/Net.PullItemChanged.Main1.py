# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to item changes and obtain the events by pulling them.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *


# Instantiate the client object
client = EasyDAClient()
# In order to use event pull, you must set a non-zero queue capacity upfront.
client.PullItemChangedQueueCapacity = 1000

print('Subscribing item changes...')
IEasyDAClientExtension.SubscribeItem(client, '', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000)

print('Processing item changes for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    eventArgs = IEasyDAClientExtension.PullItemChanged(client, 2*1000)
    if eventArgs is not None:
        # Handle the notification event
        print(eventArgs)

print('Unsubscribing item changes...')
client.UnsubscribeAllItems()

print('Finished.')

##endregion Example
