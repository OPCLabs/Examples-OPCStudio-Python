# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain a structure containing property values for an OPC item, and display some property
# values.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.Extensions import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Get a structure containing values of all well-known properties.
try:
    itemPropertyRecord = IEasyDAClientExtension2.GetItemPropertyRecord(client,
                                                                       '', 'OPCLabs.KitServer.2', 'Simulation.Random')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display some of the obtained property values.
print('itemPropertyRecord.AccessRights: ', itemPropertyRecord.AccessRights, sep='')
print('itemPropertyRecord.DataType: ', itemPropertyRecord.DataType, sep='')
print('itemPropertyRecord.Timestamp: ', itemPropertyRecord.Timestamp, sep='')

print('Finished.')

##endregion Example
