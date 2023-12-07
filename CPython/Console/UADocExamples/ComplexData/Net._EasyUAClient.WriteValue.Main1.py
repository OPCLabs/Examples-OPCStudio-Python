# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to write complex data with OPC UA Complex Data plug-in.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.BaseLib.DataTypeModel import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# [ObjectsFolder]/Data.Static.Scalar.StructureValue
nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10239')

# Instantiate the client object.
client = EasyUAClient()

# Read a node which returns complex data.
# We know that this node returns complex data, so we can type cast to UAGenericObject.
try:
    print('Reading...')
    genericObject = IEasyUAClientExtension.ReadValue(client, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Modify the data read.
# This node returns one of the two data types, randomly (this is not common, usually the type is fixed). The
# data types are sub-types of one common type which the data type of the node. We therefore use the data type
# ID in the returned UAGenericObject to detect which data type has been returned.
#
# For processing the internals of the data, refer to examples for GenericData and DataType classes.
# We know how the data is structured, and have hard-coded a logic that modifies certain values inside. It is
# also possible to discover the structure of the data type in the program, and write generic clients that can
# cope with any kind of complex data.
#
# Note that the code below is not fully robust - it will throw an exception if the data is not as expected.
print ('Modifying...')
print(genericObject.DataTypeId)
if genericObject.DataTypeId.NodeDescriptor.Match(UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=9440')):  # ScalarValueDataType
    # Negate the byte in the "ByteValue" field.
    structuredData = genericObject.GenericData
    byteValue = structuredData.FieldData.get_Item('ByteValue')  # PrimitiveData
    byteValue.Value = (~byteValue.Value) & 0xFF
    print(byteValue.Value)
elif genericObject.DataTypeId.NodeDescriptor.Match(UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=9669')): # ArrayValueDataType
    # Negate bytes at indexes 0 and 1 of the array in the "ByteValue" field.
    structuredData = genericObject.GenericData
    byteValue = structuredData.FieldData.get_Item('ByteValue')  # SequenceData
    element0 = byteValue.Elements.get_Item(0)    # PrimitiveData
    element1 = byteValue.Elements.get_Item(1)    # PrimitiveData
    element0.Value = (~element0.Value) & 0xFF
    element1.Value = (~element1.Value) & 0xFF
    print(element0.Value)
    print(element1.Value)


# Write the modified complex data back to the node.
# The data type ID in the UAGenericObject is borrowed without change from what we have read, so that the server
# knows which data type we are writing. The data type ID not necessary if writing precisely the same data type
# as the node has (not a subtype).
try:
    print('Writing...')
    IEasyUAClientExtension.WriteValue(client, endpointDescriptor, nodeDescriptor, genericObject)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)


print()
print('Finished.')

##endregion Example
