# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain a data type of an OPC item.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

# Get the value of DataType property; it is a 16-bit signed integer.
try:
    dataType = IEasyDAClientExtension.GetPropertyValue(client,
        '', 'OPCLabs.KitServer.2', 'Simulation.Random', DAPropertyId(DAPropertyIds.DataType))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()
# Convert the data type to VarType.
varType = VarType(dataType)

# Display the obtained data type.
print('DataType: ', dataType, sep='')   # Display data type as numerical value
print('VarType: ', varType, sep='')     # Display data type symbolically

# Code below illustrates how decisions can be made based on type
if varType.InternalValue == VarTypes.R8:
    print('The data type is VarTypes.R8, as we expected.')
# other cases may come here ...
else:
    print('The data type is not as we expected!')

##endregion Example
