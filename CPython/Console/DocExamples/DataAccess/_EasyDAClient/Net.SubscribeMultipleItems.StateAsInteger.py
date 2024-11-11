# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how subscribe to changes of multiple items and display each change, identifying the different
# subscriptions by an integer.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Item changed event handler.
def itemChanged(sender, eventArgs):
    # Obtain the integer state we have passed in.
    stateAsInteger = int(eventArgs.Arguments.State)
    if eventArgs.Succeeded:
        print(stateAsInteger, ': ', eventArgs.Vtq, sep='')
    else:
        print(stateAsInteger, ' *** Failure: ', eventArgs.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()
# Hook events.
client.ItemChanged += itemChanged

print('Subscribing item changes...')
handleArray = IEasyDAClientExtension.SubscribeMultipleItems(client, [
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000,
                         1),    # an integer we have chosen to identify the subscription
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 1000,
                         2),    # an integer we have chosen to identify the subscription
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000,
                         3),    # an integer we have chosen to identify the subscription
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 1000,
                         4),    # an integer we have chosen to identify the subscription
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
