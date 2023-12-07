# $Header: $
# # Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
# ##region Example
# This example shows information available about OPC event category.

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
    print('Information about category ', categoryElement, sep='')
    print('    .CategoryId: ', categoryElement.CategoryId, sep='')
    print('    .Description: ', categoryElement.Description, sep='')
    print('    .ConditionElements:')
    if categoryElement.ConditionElements.Keys is not None:
        for conditionKey in categoryElement.ConditionElements.Keys:
            print('        ', conditionKey, sep='')
    print('    .AttributeElements:')
    if categoryElement.AttributeElements.Keys is not None:
        for attributeKey in categoryElement.AttributeElements.Keys:
            print('        ', attributeKey, sep='')

##endregion Example
