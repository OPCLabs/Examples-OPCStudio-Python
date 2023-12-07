# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to wait on an item until a value with "good" quality becomes available.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.Extensions import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object
client = EasyDAClient()

print('Waiting until an item value with "good" quality becomes available...')
try:
    value = IEasyDAClientExtension2.WaitForItemValue(client, '', 'OPCLabs.KitServer.2',
                                                     DAItemDescriptor('Demo.Unreliable'),
                                                     DAGroupParameters(100),    # this is the requested update rate
                                                     60*1000)    # timeout in milliseconds
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Display the obtained item value.
print('value: ', value, sep='')

##endregion Example
