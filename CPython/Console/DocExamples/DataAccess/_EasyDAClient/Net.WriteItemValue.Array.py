# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to write into an OPC item that is of array type, and read the array value back.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

print('Writing array value...')
try:
    IEasyDAClientExtension.WriteItemValue(client, '', 'OPCLabs.KitServer.2', 'Simulation.Register_ArrayOfI2',
                                          [1234, 2345, 3456])
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('Reading array value...')
try:
    value = IEasyDAClientExtension.ReadItemValue(client, '', 'OPCLabs.KitServer.2', 'Simulation.Register_ArrayOfI2')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

if value is not None:
    print(value[0])
    print(value[1])
    print(value[2])

print('Finished.')

##endregion Example
