# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read a single item using a browse path, and display its value, timestamp and quality.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.Navigation import *
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Perform the operation.
try:
    vtq = IEasyDAClientExtension.ReadItem(client,
                                          ServerDescriptor('', 'OPCLabs.KitServer.2'),
                                          DAItemDescriptor(None, BrowsePath('/Simulation/Random')))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results.
print('Vtq: ', vtq, sep='')

##endregion Example
