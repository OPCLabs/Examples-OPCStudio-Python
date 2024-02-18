# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to write into multiple OPC items using a single method call, specifying their requested data types.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

print('Writing multiple item values...')
arguments1 = DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'),
                                  DAItemDescriptor('Simulation.Register_I2'),
                                  12345)
arguments1.ItemDescriptor.RequestedDataType = VarType(VarTypes.I2)  # <-- the requested data type
arguments2 = DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'),
                                  DAItemDescriptor('Simulation.Register_R4'),
                                  234.56)
arguments2.ItemDescriptor.RequestedDataType = VarType(VarTypes.R4)  # <-- the requested data type
operationResultArray = client.WriteMultipleItemValues([arguments1, arguments2])

for i, operationResult in enumerate(operationResultArray):
    assert operationResult is not None
    if operationResult.Succeeded:
        print('operationResultArray[', i, ']: success', sep='')
    else:
        assert operationResult.Exception is not None
        print('operationResultArray[', i, '] *** Failure: ', operationResult.ErrorMessageBrief, sep='')

print('Reading multiple item values...')
try:
    valueResultArray = IEasyDAClientExtension.ReadMultipleItemValues(client, ServerDescriptor('OPCLabs.KitServer.2'), [
        DAItemDescriptor('Simulation.Register_I2'),
        DAItemDescriptor('Simulation.Register_R4'),
    ])
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

for i, valueResult in enumerate(valueResultArray):
    assert valueResult is not None
    if valueResult.Succeeded:
        print('valueResultArray[', i, '].Value: ', valueResult.Value, sep='')
    else:
        assert valueResult.Exception is not None
        print('valueResultArray[', i, '] *** Failure: ', valueResult.ErrorMessageBrief, sep='')

print('Finished.')

##endregion Example
