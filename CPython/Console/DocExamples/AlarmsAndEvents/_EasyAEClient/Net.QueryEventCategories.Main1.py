# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to enumerate all event categories provided by the OPC server. For each category, it displays
# its Id and description.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyAEClient()

# Perform the operation
try:
    categoryElements = IEasyAEClientExtension.QueryEventCategories(client, '', 'OPCLabs.KitEventServer.2')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
for categoryElement in categoryElements:
    assert categoryElement is not None
    print('CategoryElements[', categoryElement.CategoryId, '].Description: ', categoryElement.Description, sep='')

##endregion Example
