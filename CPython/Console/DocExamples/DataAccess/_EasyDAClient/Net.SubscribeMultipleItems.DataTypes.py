# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how different data types can be subscribed to, including rare types and arrays of values.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Item changed event handler.
def itemChanged(sender, e):
    print()
    print('Arguments.ItemDescriptor.ItemId: ', e.Arguments.ItemDescriptor.ItemId, sep='')

    if e.Succeeded:
        assert e.Vtq is not None
        print('Vtq: ', e.Vtq, sep='')
    else:
        print(' *** Failure: ', e.ErrorMessageBrief, sep='')


#
itemIds = [
    'Simulation.Register_EMPTY',
    'Simulation.Register_NULL',
    'Simulation.Register_DISPATCH',

    'Simulation.ReadValue_I2',
    'Simulation.ReadValue_I4',
    'Simulation.ReadValue_R4',
    'Simulation.ReadValue_R8',
    'Simulation.ReadValue_CY',
    'Simulation.ReadValue_DATE',
    'Simulation.ReadValue_BSTR',
    'Simulation.ReadValue_BOOL',
    'Simulation.ReadValue_DECIMAL',
    'Simulation.ReadValue_I1',
    'Simulation.ReadValue_UI1',
    'Simulation.ReadValue_UI2',
    'Simulation.ReadValue_UI4',
    'Simulation.ReadValue_INT',
    'Simulation.ReadValue_UINT',

    'Simulation.ReadValue_ArrayOfI2',
    'Simulation.ReadValue_ArrayOfI4',
    'Simulation.ReadValue_ArrayOfR4',
    'Simulation.ReadValue_ArrayOfR8',
    'Simulation.ReadValue_ArrayOfCY',
    'Simulation.ReadValue_ArrayOfDATE',
    'Simulation.ReadValue_ArrayOfBSTR',
    'Simulation.ReadValue_ArrayOfBOOL',
    # 'Simulation.ReadValue_ArrayOfDECIMAL',
    'Simulation.ReadValue_ArrayOfI1',
    'Simulation.ReadValue_ArrayOfUI1',
    'Simulation.ReadValue_ArrayOfUI2',
    'Simulation.ReadValue_ArrayOfUI4',
    'Simulation.ReadValue_ArrayOfINT',
    'Simulation.ReadValue_ArrayOfUINT',
]
arguments = map(lambda itemId: DAItemGroupArguments('', 'OPCLabs.KitServer.2', itemId, 3*1000, None), itemIds)

# Instantiate the client object.
client = EasyDAClient()
client.ItemChanged += itemChanged

print('Subscribing item changes...')
IEasyDAClientExtension.SubscribeMultipleItems(client, arguments)

print('Processing item change notifications for 30 seconds...')
time.sleep(30)

print('Unsubscribing all items...')
client.UnsubscribeAllItems()

client.ItemChanged -= itemChanged
print('Finished.')

##endregion Example
