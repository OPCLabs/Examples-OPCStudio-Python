# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how subscribe to changes of a single item and display the value of the item with each change,
# using a regular callback method.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *


# Item changed callback.
def itemChangedCallback(sender, e):
    assert e is not None
    if e.Succeeded:
        assert e.Vtq is not None
        print(e.Vtq)
    else:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()

print('Subscribing item changes...')
# The callback is a regular method that displays the value.
IEasyDAClientExtension.SubscribeItem(client,
                                     '', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000,
                                     EasyDAItemChangedEventHandler(itemChangedCallback))

print('Processing item change callbacks for 10 seconds...')
time.sleep(10)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
