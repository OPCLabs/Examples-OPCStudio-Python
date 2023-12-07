# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how subscribe to changes of a single item in an OPC XML-DA server and display the value of the item
# with each change, using a callback method.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Item changed callback
def itemChanged(sender, e):
    assert e is not None
    if e.Succeeded:
        assert e.Vtq is not None
        print(e.Vtq)
    else:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object
client = EasyDAClient()

print('Subscribing item changes...')
IEasyDAClientExtension.SubscribeItem(client,
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    DAItemDescriptor('Dynamic/Analog Types/Int'),
    DAGroupParameters(1000),
    EasyDAItemChangedEventHandler(itemChanged),
    None)

print('Processing item changed events for 30 seconds...')
time.sleep(30)

print('Unsubscribing item changes...')
client.UnsubscribeAllItems()

print('Finished.')

##endregion Example
