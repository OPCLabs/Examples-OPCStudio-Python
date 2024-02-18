# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how to get value of multiple OPC XML-DA properties, and handle errors.

# Note that some properties may not have a useful value initially (e.g. until the item is activated in a group), which also the
# case with Timestamp property as implemented by the demo server. This behavior is server-dependent, and normal. You can run 
# IEasyDAClient.ReadMultipleItemValues.Main.vbs shortly before this example, in order to obtain better property values. Your 
# code may also subscribe to the items in order to assure that they remain active.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

serverDescriptor = ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx')

# Get the values of Timestamp and AccessRights properties of two items.
results = client.GetMultiplePropertyValues(
    [
        DAPropertyArguments(serverDescriptor, DANodeDescriptor('Dynamic/Analog Types/Int'), DAPropertyDescriptor.Timestamp),
        DAPropertyArguments(serverDescriptor, DANodeDescriptor('Dynamic/Analog Types/Int'), DAPropertyDescriptor.AccessRights),
        DAPropertyArguments(serverDescriptor, DANodeDescriptor('Static/Analog Types/Double'), DAPropertyDescriptor.Timestamp),
        DAPropertyArguments(serverDescriptor, DANodeDescriptor('Static/Analog Types/Double'), DAPropertyDescriptor.AccessRights)
    ])

for i, valueResult in enumerate(results):
    if valueResult.Exception is None:
        print('results[', i, '].Value: ', valueResult.Value, sep='')
    else:
        print('results[', i, '].Exception.Message: ', valueResult.Exception.Message, sep='')

##endregion Example
