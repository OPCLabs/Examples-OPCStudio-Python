# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows information available about OPC event attribute.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyAEClient()

try:
    categoryElements = IEasyAEClientExtension.QueryEventCategories(client, '', 'OPCLabs.KitEventServer.2')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

# Display results
for categoryElement in categoryElements:
    assert categoryElement is not None
    print('Category ', categoryElement, ':', sep='')
    for attributeElement in categoryElement.AttributeElements:
        assert attributeElement is not None
        print('    Information about attribute ', attributeElement, ':', sep='')
        print('        .AttributeId: ', attributeElement.AttributeId, sep='')
        print('        .Description: ', attributeElement.Description, sep='')
        print('        .DataType: ', attributeElement.DataType, sep='')

##endregion Example
