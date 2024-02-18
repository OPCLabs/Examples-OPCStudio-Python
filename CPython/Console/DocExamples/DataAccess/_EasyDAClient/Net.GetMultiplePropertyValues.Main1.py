# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to get value of multiple OPC properties, and handle errors.
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
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


serverDescriptor = ServerDescriptor('OPCLabs.KitServer.2')

# Instantiate the client object.
client = EasyDAClient()

# Get the values of Timestamp and AccessRights properties of two items.
resultArray = client.GetMultiplePropertyValues([
    DAPropertyArguments(serverDescriptor, DAItemDescriptor('Simulation.Random'), DAPropertyDescriptor.Timestamp),
    DAPropertyArguments(serverDescriptor, DAItemDescriptor('Simulation.Random'), DAPropertyDescriptor.AccessRights),
    DAPropertyArguments(serverDescriptor, DAItemDescriptor('Trends.Ramp (1 min)'), DAPropertyDescriptor.Timestamp),
    DAPropertyArguments(serverDescriptor, DAItemDescriptor('Trends.Ramp (1 min)'), DAPropertyDescriptor.AccessRights),
    ])

# Display results
for i, valueResult in enumerate(resultArray):
    valueResult = resultArray[i]
    if valueResult.Exception is None:
        print('resultArray[', i, '].Value: ', valueResult.Value, sep='')
    else:
        print('resultArray[', i, '].Exception.Message: ', valueResult.Exception.Message, sep='')

##endregion Example
