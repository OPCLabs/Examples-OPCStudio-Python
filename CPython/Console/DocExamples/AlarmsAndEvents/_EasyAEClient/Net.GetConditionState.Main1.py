# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain current state information for the condition instance corresponding to a Source and 
# certain ConditionName.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyAEClient()

print('Getting condition state...')
try:
    conditionState = IEasyAEClientExtension.GetConditionState(client,
        '', 'OPCLabs.KitEventServer.2', 'Simulation.ConditionState1', 'Simulated')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

print('ConditionState:')
print('    .ActiveSubcondition: ', conditionState.ActiveSubcondition)
print('    .Enabled: ', conditionState.Enabled)
print('    .Active: ', conditionState.Active)
print('    .Acknowledged: ', conditionState.Acknowledged)
print('    .Quality: ', conditionState.Quality)
# Note that IAEConditionState has many more properties

print()
print('Finished.')

##endregion Example
