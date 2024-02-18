# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how subscribe to changes of a single item with percent deadband.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
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


PERCENT_DEADBAND = 5.0

# Instantiate the client object
client = EasyDAClient()

print('Subscribing with ', PERCENT_DEADBAND, '% deadband...', sep='')
# The callback is a regular method that displays the value.
IEasyDAClientExtension.SubscribeItem(client,
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    DAItemDescriptor('Dynamic/Analog Types/Double', VarType(VarTypes.Empty)),
    DAGroupParameters(100, PERCENT_DEADBAND),
    EasyDAItemChangedEventHandler(itemChanged),
    None)

print('Processing item changed events for 10 seconds...')
time.sleep(10)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

print('Waiting for 2 seconds...')
time.sleep(2)

##endregion Example
