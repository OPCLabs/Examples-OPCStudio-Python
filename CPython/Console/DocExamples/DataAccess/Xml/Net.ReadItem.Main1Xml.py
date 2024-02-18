# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read a single item, and display its value, timestamp and quality.
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

# Perform the operation.
try:
    vtq = IEasyDAClientExtension.ReadItem(client, ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Dynamic/Analog Types/Int'))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

# Display results.
print('Vtq: ', vtq, sep='')

##endregion Example
