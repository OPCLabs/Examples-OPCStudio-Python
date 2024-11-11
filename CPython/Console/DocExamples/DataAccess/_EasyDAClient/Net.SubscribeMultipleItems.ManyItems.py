# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how subscribe to large number of items.
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
def itemChanged(sender, e):
    if e.Succeeded:
        print(e.Arguments.ItemDescriptor.ItemId, ': ', e.Vtq, sep='')
    else:
        print(e.Arguments.ItemDescriptor.ItemId, ' *** Failure: ', e.ErrorMessageBrief, sep='')


NUMBER_OF_ITEMS = 1000

# Instantiate the client object.
client = EasyDAClient()

client.ItemChanged += itemChanged

print('Creating array of arguments...')
argumentArray = [None]*NUMBER_OF_ITEMS
for i in range(NUMBER_OF_ITEMS):
    copy = (i//100) + 1
    phase = i % 100
    itemId = 'Simulation.Incrementing.Copy_{}.Phase_{}'.format(copy, phase)
    print(itemId)
    #
    itemGroupArguments = DAItemGroupArguments('', 'OPCLabs.KitServer.2', itemId, 50, None)
    argumentArray[i] = itemGroupArguments

print('Subscribing to changes of ', NUMBER_OF_ITEMS, ' items...')
IEasyDAClientExtension.SubscribeMultipleItems(client, argumentArray)

print('Processing item change notifications for 1 minute...')
time.sleep(60)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
