# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to enumerate all properties of an OPC item. For each property, it displays its Id and
# description.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Perform the operation.
try:
    propertyElements = IEasyDAClientExtension.BrowseProperties(client, '', 'OPCLabs.KitServer.2', 'Simulation.Random')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results.
for propertyElement in propertyElements:
    print('PropertyElements[', propertyElement.PropertyId.NumericalValue, '].Description: ', propertyElement.Description,
          sep='')

##endregion Example
