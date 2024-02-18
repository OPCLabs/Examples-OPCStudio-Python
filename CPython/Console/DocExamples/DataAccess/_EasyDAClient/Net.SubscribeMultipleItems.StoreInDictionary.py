# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to store current state of the subscribed items in a dictionary.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import threading
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


lock = threading.Lock()
vtqResultDictionary = {}

# Item changed event handler.
def itemChanged(sender, eventArgs):
    global lock
    global vtqResultDictionary
    with lock:
        # Convert the event arguments to a DAVtq result object, and store it in the dictionary under the key which
        # is the item descriptor of the item this item changed event is for.
        vtqResultDictionary[eventArgs.Arguments.ItemDescriptor] = EasyDAItemChangedEventArgs.ToDAVtqResult(eventArgs)


# Instantiate the client object.
client = EasyDAClient()
# Hook events.
client.ItemChanged += itemChanged

print('Subscribing item changes...')
handleArray = IEasyDAClientExtension.SubscribeMultipleItems(client, [
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Random', 1000, None),
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 1000, None),
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Trends.Sine (1 min)', 1000, None),
    DAItemGroupArguments('', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 1000, None),
    ])

for i in range(len(handleArray)):
    print('handleArray[', i, ']: ', handleArray[i], sep='')

print('Processing item change notifications for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    time.sleep(5)
    #
    # Each 5 seconds, display the current state of the items we have subscribed to.
    with lock:
        print()
        print('Current state of the items:')
        for itemDescriptor, vtqResult in vtqResultDictionary.items():
            print(itemDescriptor, ': ', vtqResult, sep='')
        #
        # The code above shows how you can process the complete contents of the dictionary. In other
        # scenarios, you may want to access just a specific entry in the dictionary. You can achieve that
        # by indexing the dictionary by the item descriptor of the item you are interested in.

print()
print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
