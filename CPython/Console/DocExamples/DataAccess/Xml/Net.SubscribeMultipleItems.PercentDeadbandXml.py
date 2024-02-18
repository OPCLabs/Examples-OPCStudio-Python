# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how subscribe to changes of multiple items with percent deadband.
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


# Item changed event handler
def itemChanged(sender, e):
    if e.Succeeded:
        print(e.Arguments.ItemDescriptor.ItemId, ': ', e.Vtq, sep='')
    else:
        print(e.Arguments.ItemDescriptor.ItemId, ' *** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object
client = EasyDAClient()
client.ItemChanged += itemChanged

print('Subscribing with different percent deadbands...')
IEasyDAClientExtension.SubscribeMultipleItems(client,
    [
        DAItemGroupArguments(
            ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
            DAItemDescriptor('Dynamic/Analog Types/Int', VarType(VarTypes.Empty)),
            DAGroupParameters(100, 10.0),
            None),
        DAItemGroupArguments(
            ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
            DAItemDescriptor('Dynamic/Analog Types/Double', VarType(VarTypes.Empty)),
            DAGroupParameters(100, 5.0),
            None),
    ])

print('Processing item change notifications for 1 minute...')
time.sleep(60)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
