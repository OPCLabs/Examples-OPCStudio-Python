# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain a dictionary of OPC property values for an OPC item, and extract property values.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.Extensions import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Get dictionary of property values, for all well-known properties.
try:
    propertyValueDictionary = IEasyDAClientExtension2.GetPropertyValueDictionary(client,
        '', 'OPCLabs.KitServer.2', 'Simulation.Random')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display some of the obtained property values.
# The production code should also check for the .Exception first, before getting .Value
print('propertyValueDictionary[DAPropertyId.AccessRights].Value: ',
    propertyValueDictionary.get_Item(DAPropertyId(DAPropertyIds.AccessRights)).Value, sep='')
print('propertyValueDictionary[DAPropertyId.DataType].Value: ',
    propertyValueDictionary.get_Item(DAPropertyId(DAPropertyIds.DataType)).Value, sep='')
print('propertyValueDictionary[DAPropertyId.Timestamp].Value: ',
    propertyValueDictionary.get_Item(DAPropertyId(DAPropertyIds.Timestamp)).Value, sep='')

print('Finished.')

##endregion Example
