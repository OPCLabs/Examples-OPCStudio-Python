# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to read a single item from the device, and display its value, timestamp and quality.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

print('Reading item...')
try:
    # DADataSource enumeration:
    # Selects the data source for OPC reads (from device, from OPC cache, or dynamically determined).
    # The data source (memory, OPC cache or OPC device) selection is based on the desired value age and
    # current status of data received from the server.
    vtq = IEasyDAClientExtension.ReadItem(client,
                                          ServerDescriptor('OPCLabs.KitServer.2'),
                                          DAItemDescriptor('Simulation.Random'),
                                          DAReadParameters(DADataSource.Device))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display results.
print('Vtq: ', vtq, sep='')

##endregion Example
