# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example subscribes to changes of 2 items separately, and displays rich information available with each item
# changed event notification.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *


# Item changed event handler.
def itemChanged(sender, e):
    assert e is not None
    print()
    print('e.Arguments.State: ', e.Arguments.State, sep='')
    print('e.Arguments.ServerDescriptor.MachineName: ', e.Arguments.ServerDescriptor.MachineName, sep='')
    print('e.Arguments.ServerDescriptor.ServerClass: ', e.Arguments.ServerDescriptor.ServerClass, sep='')
    print('e.Arguments.ItemDescriptor.ItemId: ', e.Arguments.ItemDescriptor.ItemId, sep='')
    print('e.Arguments.ItemDescriptor.AccessPath: ', e.Arguments.ItemDescriptor.AccessPath, sep='')
    print('e.Arguments.ItemDescriptor.RequestedDataType: ', e.Arguments.ItemDescriptor.RequestedDataType, sep='')
    print('e.Arguments.GroupParameters.Locale: ', e.Arguments.GroupParameters.Locale, sep='')
    print('e.Arguments.GroupParameters.RequestedUpdateRate: ', e.Arguments.GroupParameters.RequestedUpdateRate, sep='')
    print('e.Arguments.GroupParameters.PercentDeadband: ', e.Arguments.GroupParameters.PercentDeadband, sep='')
    if e.Succeeded:
        assert e.Vtq is not None
        print('e.Vtq.Value: ', e.Vtq.Value, sep='')
        print('e.Vtq.Timestamp: ', e.Vtq.Timestamp, sep='')
        print('e.Vtq.TimestampLocal: ', e.Vtq.TimestampLocal, sep='')
        print('e.Vtq.Quality: ', e.Vtq.Quality, sep='')
    else:
        assert e.Exception is not None
        print('e.Exception.Message: ', e.Exception.Message, sep='')
        print('e.Exception.Source: ', e.Exception.Source, sep='')


# Instantiate the client object.
client = EasyDAClient()

client.ItemChanged += itemChanged

print('Subscribing item changes for 2 items...')
IEasyDAClientExtension.SubscribeItem(client, '', 'OPCLabs.KitServer.2', 'Simulation.Random', 5*1000)
IEasyDAClientExtension.SubscribeItem(client, '', 'OPCLabs.KitServer.2', 'Trends.Ramp (1 min)', 5*1000)

print('Processing item change notifications for 1 minute...')
time.sleep(60)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
