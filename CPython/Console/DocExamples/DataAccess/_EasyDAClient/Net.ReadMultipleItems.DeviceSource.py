# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read 4 items from the device, and display their values, timestamps and qualities.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# DADataSource enumeration:
# Selects the data source for OPC reads (from device, from OPC cache, or dynamically determined).
# The data source (memory, OPC cache or OPC device) selection is based on the desired value age and
# current status of data received from the server.

#
vtqResultArray = client.ReadMultipleItems([
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Random'), DAReadParameters(DADataSource.Device)),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Ramp (1 min)'), DAReadParameters(DADataSource.Device)),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Trends.Sine (1 min)'), DAReadParameters(DADataSource.Device)),
    DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor('Simulation.Register_I4'), DAReadParameters(DADataSource.Device)),
    ])

for i, vtqResult in enumerate(vtqResultArray):
    assert vtqResult is not None
    if vtqResult.Succeeded:
        print('vtqResultArray[', i, '].Vtq: ', vtqResult.Vtq, sep='')
    else:
        print('vtqResultArray[', i, '] *** Failure: ', vtqResult.ErrorMessageBrief, sep='')

##endregion Example
