# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how subscribe to changes of multiple items and display each change, identifying the different
# subscriptions by an object.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


class CustomObject(object):
    def __init__(self, name):
        self.name = name


# Item changed event handler.
def itemChanged(sender, eventArgs):
    # Obtain the custom object we have passed in.
    stateAsObject = eventArgs.Arguments.State
    if eventArgs.Succeeded:
        print(stateAsObject.name, ': ', eventArgs.Vtq, sep='')
    else:
        print(stateAsObject.name, ' *** Failure: ', eventArgs.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()
# Hook events.
client.ItemChanged += itemChanged

print('Subscribing item changes...')
handleArray = IEasyDAClientExtension.SubscribeMultipleItems(client, [
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000,
                         CustomObject('First')),    # a custom object that corresponds to the subscription
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 1000,
                         CustomObject('Second')),   # a custom object that corresponds to the subscription
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000,
                         CustomObject('Third')),    # a custom object that corresponds to the subscription
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 1000,
                         CustomObject('Fourth')),   # a custom object that corresponds to the subscription
    ])

for i in range(len(handleArray)):
    print('handleArray[', i, ']: ', handleArray[i], sep='')

print('Processing item change notifications for 1 minute...')
time.sleep(60)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
