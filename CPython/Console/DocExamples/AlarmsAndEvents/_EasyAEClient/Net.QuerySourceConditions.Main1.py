# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to enumerate all event conditions associated with the specified event source.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyAEClient()

# Perform the operation.
try:
    conditionElements = IEasyAEClientExtension.QuerySourceConditions(client, '', 'OPCLabs.KitEventServer.2',
                                                                     AENodeDescriptor('Simulation.ConditionState1'))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results.
for conditionElement in conditionElements:
    assert conditionElement is not None
    print('ConditionElements[', conditionElement.Name, ']: ',
          conditionElement.SubconditionNames.Length, ' subcondition(s)',
          sep='')

print()
print('Finished.')

##endregion Example
