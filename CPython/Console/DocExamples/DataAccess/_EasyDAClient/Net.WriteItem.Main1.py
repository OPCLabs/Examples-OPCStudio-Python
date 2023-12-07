# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to write a value, timestamp and quality into a single item.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Perform the operation
try:
    IEasyDAClientExtension.WriteItem(client, '', 'OPCLabs.KitServer.2', 'Simulation.Register_I4',
                                     12345, DateTime.SpecifyKind(DateTime(1980, 1, 1), DateTimeKind.Utc),
                                     DAQuality(192))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
