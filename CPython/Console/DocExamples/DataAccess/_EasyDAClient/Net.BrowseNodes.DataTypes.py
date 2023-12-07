# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain data types of leaves in the OPC-DA address
# space by browsing and filtering, i.e. without the use of OPC properties.
# This technique allows determining the data types with servers that only
# support OPC-DA 1.0. It can also be more effective than the use of
# GetMultiplePropertyValues, if there is large number of leaves, and
# relatively small number of data types to be checked.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.ComInterop import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *

# Instantiate the client object.
client = EasyDAClient()

# Define the list of data types we will be checking for.
# Change as needed for your application.
# This technique is only usable if there is a known list of
# data types you are interested in. If you are interested in
# all leaves, even those that are of data types not explicitly
# listed, always include VarTypes.Empty as the first data type.
# The leaves of "unlisted" data types will have VarTypes.Empty
# associated with them.
dataTypes = [VarType(VarTypes.Empty), VarType(VarTypes.I2), VarType(VarTypes.R4)]

# For each leaf found, this dictionary wil hold its associated data type.
dataTypeDictionary = {}

# For each data type, browse for leaves of this data type.
for dataType in dataTypes:
    browseParameters = DABrowseParameters(DABrowseFilter.Leaves, '', '', dataType)
    try:
        nodeElements = IEasyDAClientExtension.BrowseNodes(client,
                                                          '', 'OPCLabs.KitServer.2', 'Greenhouse', browseParameters)
    except OpcException as opcException:
        print('*** Failure: ' + opcException.GetBaseException().Message)
        exit()

    # Store the leaf information into the dictionary, and
    # associate the current data type with it.
    for nodeElement in nodeElements:
        dataTypeDictionary[nodeElement] = dataType

# Display each leaf found, and its associated data type.
for nodeElement, dataType in dataTypeDictionary.items():
    print(nodeElement, ': ', dataType, sep='')

##endregion Example
