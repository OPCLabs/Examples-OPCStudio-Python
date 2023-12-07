# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to create and use two isolated client objects, resulting in two separate connections to the
# target OPC DA server.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *


# Item changed event handler
def itemChangedCallback(sender, eventArgs):
    assert eventArgs is not None
    print('[', eventArgs.Arguments.State, '] ', sep='', end='')
    if eventArgs.Succeeded:
        assert eventArgs.Vtq is not None
        print(eventArgs.Vtq)
    else:
        print('*** Failure: ', eventArgs.ErrorMessageBrief, sep='')


# Instantiate the client objects and make them isolated.
client1 = EasyDAClient()
client1.Isolated = True
client2 = EasyDAClient()
client2.Isolated = True

print('Subscribing item changes...')
IEasyDAClientExtension.SubscribeItem(client1,
                                     '', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000,
                                     EasyDAItemChangedEventHandler(itemChangedCallback), 1)
IEasyDAClientExtension.SubscribeItem(client2,
                                     '', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000,
                                     EasyDAItemChangedEventHandler(itemChangedCallback), 2)

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Unsubscribing all items...')
client1.UnsubscribeAllItems()
client2.UnsubscribeAllItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
