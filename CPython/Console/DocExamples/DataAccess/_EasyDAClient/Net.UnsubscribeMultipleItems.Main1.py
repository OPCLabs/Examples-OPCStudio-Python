# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to unsubscribe from changes of multiple items.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from System.Collections.Generic import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Item changed event handler.
def itemChanged(sender, e):
    if e.Succeeded:
        print(e.Arguments.ItemDescriptor.ItemId, ': ', e.Vtq, sep='')
    else:
        print(e.Arguments.ItemDescriptor.ItemId, ' *** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()

client.ItemChanged += itemChanged

print('Subscribing item changes...')
handleArray = client.SubscribeMultipleItems([
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 1000, None),
    ])

for i in range(len(handleArray)):
    print('handleArray[', i, ']: ', handleArray[i], sep='')

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Unsubscribing from two items...')
handleList = List[int]()
handleList.Add(handleArray[1])
handleList.Add(handleArray[2])
client.UnsubscribeMultipleItems(handleList)

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Unsubscribing from all remaining items...')
client.UnsubscribeAllItems()

print('Waiting for 5 seconds...')
time.sleep(5)

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
