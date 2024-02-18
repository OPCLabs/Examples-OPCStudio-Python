# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how change the percent deadband of an existing subscription.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc.DataAccess import *


# Item changed event handler
def itemChanged(sender, e):
    if e.Succeeded:
        print(e.Vtq)
    else:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')


# Instantiate the client object.
client = EasyDAClient()

client.ItemChanged += itemChanged

print('Subscribing item with 10% deadband...')
handle = IEasyDAClientExtension.SubscribeItem(client, '', 'OPCLabs.KitServer.2', 'Simulation.Ramp 0:100 (10 s)',
                                              VarType(VarTypes.Empty), requestedUpdateRate=50, percentDeadband=10.0,
                                              state=None)

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Changing item subscription to 0% deadband...')
IEasyDAClientExtension.ChangeItemSubscription(client, handle, DAGroupParameters(50, 0.0))

print('Processing item change notifications for 10 seconds...')
time.sleep(10)

print('Unsubscribing item...')
IEasyDAClientExtension.UnsubscribeItem(client, handle)

print('Waiting for 10 seconds...')
time.sleep(10)

client.ItemChanged -= itemChanged

print('Finished.')

##endregion Example
