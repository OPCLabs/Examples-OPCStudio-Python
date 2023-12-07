# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read items while subscribed.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Item changed event handler.
def itemChanged(sender, e):
    if e.Succeeded:
        print('< ', e.Arguments.ItemDescriptor.ItemId, ': ', e.Vtq, sep='')
    else:
        print('< ', e.Arguments.ItemDescriptor.ItemId, ' *** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()

client.ItemChanged += itemChanged

print('Subscribing item changes...')
client.SubscribeMultipleItems([
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000, None),
    ])

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Reading items...')
vtqResultArray = client.ReadMultipleItems([
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Ramp (1 min)')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Sine (1 min)')),
    ])

for i, vtqResult in enumerate(vtqResultArray):
    assert vtqResult is not None
    if vtqResult.Succeeded:
        print('vtqResultArray[', i, '].Vtq: ', vtqResult.Vtq, sep='')
    else:
        print('vtqResultArray[', i, '] *** Failure: ', vtqResult.ErrorMessageBrief, sep='')

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
