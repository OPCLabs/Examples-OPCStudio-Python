# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to get a value of a single OPC property.
#
# Note that some properties may not have a useful value initially (e.g. until the item is activated in a group), which also the
# case with Timestamp property as implemented by the demo server. This behavior is server-dependent, and normal. You can run 
# IEasyDAClient.ReadItemValue.Main.vbs shortly before this example, in order to obtain better property values. Your code may 
# also subscribe to the item in order to assure that it remains active.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyDAClient()

# Perform the operation
try:
    value = IEasyDAClientExtension.GetPropertyValue(client,
        '', 'OPCLabs.KitServer.2', 'Simulation.Random', DAPropertyId(DAPropertyIds.Timestamp))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
print('value: ', value, sep='')

##endregion Example
