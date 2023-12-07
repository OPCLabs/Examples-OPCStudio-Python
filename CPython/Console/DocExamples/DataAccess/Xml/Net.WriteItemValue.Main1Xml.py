# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to write a value into a single OPC XML-DA item.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Perform the operation
try:
    IEasyDAClientExtension.WriteItemValue(client,
        ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
        DAItemDescriptor('Static/Analog Types/Int'),
        12345)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
