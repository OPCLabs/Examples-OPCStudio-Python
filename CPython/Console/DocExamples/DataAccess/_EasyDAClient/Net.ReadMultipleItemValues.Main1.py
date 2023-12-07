# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read values of 4 items at once, and display them.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

#
valueResultArray = IEasyDAClientExtension.ReadMultipleItemValues(client, [
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Random')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Ramp (1 min)')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Sine (1 min)')),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_I4')),
    ])

for i, valueResult in enumerate(valueResultArray):
    assert valueResult is not None
    if valueResult.Succeeded:
        print('valueResultArray[', i, '].Value: ', valueResult.Value, sep='')
    else:
        print('valueResultArray[', i, '] *** Failure: ', valueResult.ErrorMessageBrief, sep='')

##endregion Example
