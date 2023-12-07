# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read value of a single item, and display it, using CLSID instead of ProgID of the OPC
# Server.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyDAClient()

print('Reading item value...')
try:
    value = IEasyDAClientExtension.ReadItemValue(client,
                                                 '', '{C8A12F17-1E03-401E-B53D-6C654DD576DA}', 'Simulation.Random')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
print('value: ', value, sep='')

##endregion Example
