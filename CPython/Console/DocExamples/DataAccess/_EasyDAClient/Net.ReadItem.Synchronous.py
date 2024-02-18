# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read an item synchronously, and display its value, timestamp and quality.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Specify that only synchronous method is allowed. By default, both synchronous and asynchronous methods are
# allowed, and the component picks a suitable method automatically. Disallowing asynchronous method leaves
# only the synchronous method available for selection.
client.InstanceParameters.Mode.AllowAsynchronousMethod = False

# Perform the operation.
try:
    vtq = IEasyDAClientExtension.ReadItem(client, '', 'OPCLabs.KitServer.2', 'Simulation.Random')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

# Display results.
print('Vtq: ', vtq, sep='')

##endregion Example
