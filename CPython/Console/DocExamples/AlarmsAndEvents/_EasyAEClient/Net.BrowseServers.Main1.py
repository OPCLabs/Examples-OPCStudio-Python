# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain all ProgIDs of all OPC Alarms and Events servers on the local machine.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.AlarmsAndEvents import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyAEClient()

# Perform the operation
try:
    serverElements = IEasyAEClientExtension.BrowseServers(client, '')
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
for serverElement in serverElements:
    assert serverElement is not None
    print('ServerElements["', serverElement.ClsidString, '"]: ', serverElement.ProgId, sep='')

##endregion Example
