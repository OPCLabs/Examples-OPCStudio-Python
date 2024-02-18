# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how the OPC server can quickly be disconnected after writing a value into one of its OPC items.
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

client.InstanceParameters.HoldPeriods.TopicWrite = 100  # in milliseconds

# Perform the operation
try:
    IEasyDAClientExtension.WriteItemValue(client, '', 'OPCLabs.KitServer.2', 'Simulation.Register_I4', 12345)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
