# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to process a data type, displaying some of its properties, recursively.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.BaseLib.DataTypeModel import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def processDataType(dataType, maximumDepth):
    if maximumDepth == 0:
        print('* Reached maximum depth *')
        return

    print()
    print('dataType.Name: ', dataType.Name, sep='')

    if dataType.Kind == DataTypeKind.Enumeration:
        print('The data type is an enumeration.')
        enumerationDataType = dataType
        print('It has ', enumerationDataType.EnumerationMembers.Count, ' enumeration members.', sep='')
        print('The names of the enumeration members are: ', end='')
        for i, member in enumerate(enumerationDataType.EnumerationMembers):
            if i != 0:
                print(', ', end='')
            print(member.Name, end='')
        print('.')
        # Here you can process the members, or inspect SizeInBits etc.

    elif dataType.Kind == DataTypeKind.Opaque:
        print('The data type is opaque.')
        opaqueDataType = dataType
        print('Its size is ', opaqueDataType.SizeInBits, ' bits.', sep='')
        # There isn't much more you can learn about an opaque data type (well, it may have Description and
        # other common members). It is, after all, opaque...

    elif dataType.Kind == DataTypeKind.Primitive:
        print('The data type is primitive.')
        primitiveDataType = dataType
        print('Its .NET value type is "', primitiveDataType.ValueType, '".', sep='')
        # There isn't much more you can learn about the primitive data type.

    elif dataType.Kind == DataTypeKind.Sequence:
        print('The data type is a sequence.')
        sequenceDataType = dataType
        print('Its length is ', sequenceDataType.Length, ' (-1 means that the length can vary).', sep='')

        print('A dump of the element data type follows.')
        processDataType(sequenceDataType.ElementDataType, maximumDepth - 1)

    elif dataType.Kind == DataTypeKind.Structured:
        print('The data type is structured.')
        structuredDataType = dataType
        print('It has ', structuredDataType.DataFields.Count, ' data fields.', sep='')
        print('The names of the data fields are: ', end='')
        for i, field in enumerate(structuredDataType.DataFields):
            if i != 0:
                print(', ', end='')
            print(field.Name, end='')
        print('.')

        print('A dump of each of the data fields follows.')
        for dataField in structuredDataType.DataFields:
            print()
            print('dataField.Name: ', dataField.Name, sep='')
            # Note that every data field also has properties like IsLength, IsOptional, IsSwitch which might
            # be of interest, but we are not dumping them here.
            processDataType(dataField.DataType, maximumDepth - 1)

    elif dataType.Kind == DataTypeKind.Union:
        print('The data type is union.')
        unionDataType = dataType
        print('It has ', unionDataType.DataFields.Count, ' data fields.', sep='')
        print('The names of the data fields are: ', end='')
        for i, field in enumerate(unionDataType.DataFields):
            if i != 0:
                print(', ', end='')
            print(field.Name, end='')
        print('.')


# Define which server and node we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# [ObjectsFolder]/Data.Static.Scalar.StructureValue
nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10239')

# Instantiate the client object.
client = EasyUAClient()

# Read a node. We know that this node returns complex data, so we can type cast to UAGenericObject.
try:
    print('Reading...')
    genericObject = IEasyUAClientExtension.ReadValue(client, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()
print('Reading successful.')
# The data type is in the GenericData.DataType property of the UAGenericObject.
dataType = genericObject.GenericData.DataType

# Process the data type. We will inspect some of its properties, and dump them.
processDataType(dataType, 3)

print()
print('Finished.')

##endregion Example
