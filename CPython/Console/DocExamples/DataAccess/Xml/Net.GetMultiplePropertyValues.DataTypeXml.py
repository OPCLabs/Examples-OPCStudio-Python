# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain a data type of all OPC XML-DA items under a branch.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


serverDescriptor = ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx')

# Instantiate the client object.
client = EasyDAClient()

# Browse for all leaves under the "Static/Analog Types" branch
try:
    nodeElementCollection = IEasyDAClientExtension.BrowseLeaves(client,
                                                                serverDescriptor,
                                                                DANodeDescriptor('Static/Analog Types'))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message)
    exit()

# Create list of node descriptors, one for each leaf obtained.
filteredNodeElements = filter(lambda element: not element.IsHint, nodeElementCollection)
nodeDescriptorArray = list(map(lambda element: DANodeDescriptor(element), filteredNodeElements))

# Get the value of DataType property; it is a 16-bit signed integer.
resultArray = IEasyDAClientExtension.GetMultiplePropertyValues(client,
                                                               serverDescriptor,
                                                               nodeDescriptorArray,
                                                               DAPropertyDescriptor.FromInt64(DAPropertyIds.DataType))
# Display results
for i, valueResult in enumerate(resultArray):
    nodeDescriptor = nodeDescriptorArray[i]
    # Check if there has been an error getting the property value.
    if valueResult.Exception is  None:
        # Convert the data type to VarType.
        varType = VarType(valueResult.Value)
        # Display the obtained data type.
        print(nodeDescriptor.ItemId, ': ', varType, sep='')
    else:
        print(nodeDescriptor.ItemId, ' *** Failure: ', valueResult.Exception.Message)

print()
print('Finished')

##endregion Example
