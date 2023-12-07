# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to obtain object describing the data type of complex data node with OPC UA Complex Data plug-in.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from Microsoft.Extensions.DependencyInjection import *
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
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

# Resolve the data type ID to the data type object, containing description of the data type.
dataTypeResult = IEasyUAClientComplexDataExtension.ResolveDataType(complexData,
    UAModelNodeDescriptor(endpointDescriptor, UANodeDescriptor(dataTypeId)),
    UABrowseNames.DefaultBinary)
# Check if the operation succeeded. Use the ThrowIfFailed method instead if you want exception be thrown.
if not dataTypeResult.Succeeded:
    print('*** Failure: ', dataTypeResult.ErrorMessageBrief)
    exit()

# The actual data type is in the Value property.
# Display basic information about what we have obtained.
print(dataTypeResult.Value)

# If we want to see the whole hierarchy of the received data type, we can format it with the "V" (verbose)
# specifier. In the debugger, you can view the same by displaying the private DebugView property.
print()
print(String.Format('{0:V}', dataTypeResult.Value))

# For processing the internals of the data type, refer to examples for GenericData class.

print()
print('Finished.')

##endregion Example
