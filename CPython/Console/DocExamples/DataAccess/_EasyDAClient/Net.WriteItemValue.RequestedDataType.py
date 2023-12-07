# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to write a value into a single item, specifying its requested data type.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Perform the operation
try:
    IEasyDAClientExtension.WriteItemValue(client, '', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 12345,
                                          VarType(VarTypes.I4)) # <-- the requested data type
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
