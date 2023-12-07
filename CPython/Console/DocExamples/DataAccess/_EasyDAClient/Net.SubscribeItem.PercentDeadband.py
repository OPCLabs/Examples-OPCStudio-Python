# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how subscribe to changes of a single item with percent deadband.

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


PERCENT_DEADBAND = 5.0

# Instantiate the client object.
client = EasyDAClient()

print('Subscribing item changes with ', PERCENT_DEADBAND, '% deadband...', sep='')
# The callback is a regular method that displays the value.
IEasyDAClientExtension.SubscribeItem(client,
                                     '', 'OPCLabs.KitServer.2', 'Simulation.Ramp 0:100 (10 s)', 50,
                                     EasyDAItemChangedEventHandler(itemChangedCallback))

print('Processing item change callbacks for 10 seconds...')
time.sleep(10)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
