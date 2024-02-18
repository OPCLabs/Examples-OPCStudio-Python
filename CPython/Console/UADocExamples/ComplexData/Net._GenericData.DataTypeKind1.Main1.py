# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# Shows how to process generic data type, displaying some of its properties, recursively.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.BaseLib.DataTypeModel import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def processGenericData(genericData, maximumDepth):
    if maximumDepth == 0:
        print('* Reached maximum depth *')
        return

    print()
    print('genericData.DataType: ', genericData.DataType, sep='')

    dataTypeKind = genericData.DataTypeKind
    if dataTypeKind == DataTypeKind.Enumeration:
        print('The generic data is an enumeration.')
        enumerationData = genericData
        print('Its value is ', enumerationData.Value, '.', sep='')
        # There is also a ValueName that you can inspect (if known).

    elif dataTypeKind == DataTypeKind.Opaque:
        print('The generic data is opaque.')
        opaqueData = genericData
        print('Its size is ', opaqueData.SizeInBits, ' bits.', sep='')
        print('The data bytes are ', BitConverter.ToString(opaqueData.ByteArray), '.', sep='')
        # Use the Value property (a BitArray) if you need to access the value bit by bit.

    elif dataTypeKind == DataTypeKind.Primitive:
        print('The generic data is primitive.')
        primitiveData = genericData
        print('Its value is "', primitiveData.Value, '".', sep='')

    elif dataTypeKind == DataTypeKind.Sequence:
        print('The generic data is a sequence.')
        sequenceData = genericData
        print('It has ', sequenceData.Elements.Count, ' elements.', sep='')
        print('A dump of the elements follows.')
        for element in sequenceData.Elements:
            processGenericData(element, maximumDepth - 1)

    elif dataTypeKind == DataTypeKind.Structured:
        print('The generic data is structured.')
        structuredData = genericData
        print('It has ', structuredData.FieldData.Count, ' field data members.', sep='')
        print('The names of the fields are: ', end='')
        for i, name in enumerate(structuredData.FieldData.Keys):
            if i != 0:
                print(', ', end='')
            print(name, end='')
        print('.')

        print('A dump of each of the fields follows.')
        for pair in structuredData.FieldData:
            print()
            print('Field name: ', pair.Key, sep='')
            processGenericData(pair.Value, maximumDepth - 1)

    elif dataTypeKind == DataTypeKind.Union:
        print('The generic data is a union.')
        unionData = genericData
        print('The name of current field is: ', unionData.FieldName, sep='')
        print('Current field value is: ', unionData.FieldValue, end='')


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

# Process the generic data type. We will inspect some of its properties, and dump them.
processGenericData(genericObject.GenericData, 3)

print()
print('Finished.')

##endregion Example
