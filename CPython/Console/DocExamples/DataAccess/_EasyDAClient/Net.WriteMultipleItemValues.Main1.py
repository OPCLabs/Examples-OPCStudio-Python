# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to write into multiple OPC items using a single method call, and read multiple item values back.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
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
                         12345),
    DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_BOOL'),
                         True),
    DAItemValueArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_R4'),
                         234.56),
    ])

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
        DAItemDescriptor('Simulation.Register_I4'),
        DAItemDescriptor('Simulation.Register_BOOL'),
        DAItemDescriptor('Simulation.Register_R4'),
    ])
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

for i, valueResult in enumerate(valueResultArray):
    assert valueResult is not None
    if valueResult.Succeeded:
        print('valueResultArray[', i, '].Value: ', valueResult.Value, sep='')
    else:
        assert valueResult.Exception is not None
        print('valueResultArray[', i, '] *** Failure: ', valueResult.ErrorMessageBrief, sep='')

##endregion Example
