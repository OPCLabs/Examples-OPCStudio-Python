# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to read a value of a single item from the device and display its value.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
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
    # DADataSource enumeration:
    # Selects the data source for OPC reads (from device, from OPC cache, or dynamically determined).
    # The data source (memory, OPC cache or OPC device) selection is based on the desired value age and
    # current status of data received from the server.
    value = IEasyDAClientExtension.ReadItemValue(client,
                                                 ServerDescriptor('OPCLabs.KitServer.2'),
                                                 DAItemDescriptor('Demo.Single'),
                                                 DAReadParameters(DADataSource.Device))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

# Display results
print('value: ', value, sep='')

##endregion Example
