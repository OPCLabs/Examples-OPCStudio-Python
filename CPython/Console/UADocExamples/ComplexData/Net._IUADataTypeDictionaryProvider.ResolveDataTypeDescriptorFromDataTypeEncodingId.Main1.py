# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to obtain data type description object for complex data node with OPC UA Complex Data plug-in, and the
# actual content of the data type dictionary.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from Microsoft.Extensions.DependencyInjection import *
from System import *
from System.Text import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.DataTypeModel.Extensions import *
#from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.InformationModel import *
from OpcLabs.EasyOpc.UA.Plugins.ComplexData import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain the data type ID.
#
# In many cases, you would be able to obtain the data type ID of a particular node by reading its DataType
# attribute, or easier, by calling the extension method ReadDataType on the IEasyUAClient interface.
# The sample server, however, shows a more advanced approach in which the data type ID refers to an abstract
# data type, and the actual values are then sub-types of this base data type. This abstract data type does not
# have any encodings associated with it and it is therefore not possible to extract its description from the
# server. We therefore use a hard-coded data type ID for one of the sub-types in this example.
#
# The code to obtain the data type ID for given node would normally look like this:
#    dataTypeId = IEasyUAClientExtension2.ReadDataType(client,
#        endpointDescriptor,
#        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10239'))	# [ObjectsFolder]/Data.Static.Scalar.StructureValue
dataTypeId = UANodeId('nsu=http://test.org/UA/Data/ ;i=9440')   # ScalarValueDataType

# Get the IEasyUAClientComplexData service from the client. This is needed for advanced complex data
# operations.
complexData = ServiceProviderServiceExtensions.GetService[IEasyUAClientComplexData](client)
if complexData is None:
    print('The client complex data service is not available.')
    exit()

# Get the data type model provider. Provides methods to access data types in OPC UA model.
dataTypeModelProvider = complexData.DataTypeModelProvider

# Resolve the data type ID from our data type ID, for encoding name "Default Binary".
encodingIdResult = IUADataTypeModelProviderExtension.ResolveEncodingIdFromDataTypeId(dataTypeModelProvider,
    UAModelNodeDescriptor(endpointDescriptor, UANodeDescriptor(dataTypeId)),
    UABrowseNames.DefaultBinary)
# Check if the operation succeeded. Use the ThrowIfFailed method instead if you want exception be thrown.
if not encodingIdResult.Succeeded:
    print('*** Failure: ', encodingIdResult.ErrorMessageBrief)
    exit()
encodingId = encodingIdResult.Value

# Get the data type dictionary provider. Provides methods to access data type dictionaries in OPC UA model.
dataTypeDictionaryProvider = complexData.DataTypeDictionaryProvider

# Resolve the data type descriptor from the encoding ID.
dataTypeDescriptorResult = IUADataTypeDictionaryProviderExtension.ResolveDataTypeDescriptorFromDataTypeEncodingId(
    dataTypeDictionaryProvider, encodingId)
# Check if the operation succeeded. Use the ThrowIfFailed method instead if you want exception be thrown.
if not dataTypeDescriptorResult.Succeeded:
    print('*** Failure: ', dataTypeDescriptorResult.ErrorMessageBrief)
    exit()
dataTypeDescriptor = dataTypeDescriptorResult.Value

# The data type descriptor contains two pieces of information:
# The data type dictionary ID: This determines the dictionary where the data type is defined.
print(dataTypeDescriptor.DataTypeDictionaryId)
# And the data type description: It is a "pointer" into the data type dictionary itself, selecting a specific
# type definition inside the data type dictionary. The format of it depends on the data type system;
# in our case, it is a string that is the name of one of the type elements in the XML document of the data type
# dictionary.
print(dataTypeDescriptor.DataTypeDescription)

# Obtain the actual content of the data type dictionary.
dataTypeDictionaryResult = IUADataTypeDictionaryProviderExtension.GetDataTypeDictionaryFromDataTypeDictionaryId(
    dataTypeDictionaryProvider, dataTypeDescriptor.DataTypeDictionaryId)
# Check if the operation succeeded. Use the ThrowIfFailed method instead if you want exception be thrown.
if not dataTypeDictionaryResult.Succeeded:
    print('*** Failure: ', dataTypeDictionaryResult.ErrorMessageBrief)
    exit()
dataTypeDictionary = dataTypeDictionaryResult.Value

# The data type dictionary returned is an array of bytes; its syntax and semantics depends on the data type
# system. In our case, we know that the data type dictionary is actually a string encoded in UTF-8.
text = Encoding.UTF8.GetString(dataTypeDictionary)
print()
print(text)

print()
print('Finished.')

##endregion Example
