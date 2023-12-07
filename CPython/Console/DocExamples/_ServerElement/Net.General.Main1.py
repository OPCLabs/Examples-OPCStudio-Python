# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows all information available about OPC servers.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

try:
    serverElements = IEasyDAClientExtension.BrowseServers(client)
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results
for serverElement in serverElements:
    print('Information about server ', serverElement, ':', sep='')
    print('    .ServerClass: ', serverElement.ServerClass, sep='')
    print('    .ClsidString: ', serverElement.ClsidString, sep='')
    print('    .ProgId: ', serverElement.ProgId, sep='')
    print('    .Description: ', serverElement.Description, sep='')
    print('    .Vendor: ', serverElement.Vendor, sep='')
    print('    .ServerCategories: ', serverElement.ServerCategories, sep='')
    print('    .VersionIndependentProgId: ', serverElement.VersionIndependentProgId, sep='')

##endregion Example
