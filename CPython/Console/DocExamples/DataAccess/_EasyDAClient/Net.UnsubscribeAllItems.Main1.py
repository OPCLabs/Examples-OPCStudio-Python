# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to unsubscribe from changes of all items.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
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
client.SubscribeMultipleItems([
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000, None),
    EasyDAItemSubscriptionArguments('', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 1000, None),
    ])

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Unsubscribing from all items...')
client.UnsubscribeAllItems()

print('Waiting for 10 seconds...')
time.sleep(10)

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
