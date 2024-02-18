# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to write values, timestamps and qualities into 3 items at once.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

print('Writing multiple items...')
operationResultArray = client.WriteMultipleItems([
    DAItemVtqArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_I4'),
                       DAVtq(23456, DateTime.UtcNow, DAQuality(DAQualities.GoodNonspecific))),
    DAItemVtqArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_R8'),
                       DAVtq(2.34567890, DateTime.UtcNow, DAQuality(DAQualities.GoodNonspecific))),
    DAItemVtqArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_BSTR'),
                       DAVtq('ABC', DateTime.UtcNow, DAQuality(DAQualities.GoodNonspecific))),
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
