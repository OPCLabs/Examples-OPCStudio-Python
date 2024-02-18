# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to write values into 3 items at once, test for success of each write and display the exception
# message in case of failure.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

print('Writing multiple item values...')
operationResultArray = client.WriteMultipleItemValues([
    DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_I4'),
                         23456),
    DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_R8'),
                         'This string cannot be converted to VT_R8'),
    DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('UnknownItem'),
                         'ABC'),
    ])

for i, operationResult in enumerate(operationResultArray):
    assert operationResult is not None
    if operationResult.Succeeded:
        print('operationResultArray[', i, ']: success', sep='')
    else:
        assert operationResult.Exception is not None
        print('operationResultArray[', i, '] *** Failure: ', operationResult.ErrorMessageBrief, sep='')

print('Finished.')

##endregion Example
