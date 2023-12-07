# $Header: $
# # Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
# ##region Example
# This example shows information available about OPC event condition.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


def dumpSubconditionNames(subconditionNames):
    for name in subconditionNames:
        print('            ', name, sep='')


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
    print('Category ', categoryElement, sep='')
    for conditionElement in categoryElement.ConditionElements:
        assert  conditionElement is not None
        print('    Information about condition "', conditionElement, '":', sep='')
        print('        .Name: ', conditionElement.Name, sep='')
        print('        .SubconditionNames:')
        dumpSubconditionNames(conditionElement.SubconditionNames)

##endregion Example
