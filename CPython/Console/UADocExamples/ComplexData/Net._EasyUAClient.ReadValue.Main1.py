# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to read complex data with OPC UA Complex Data plug-in.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
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

# Read a node which returns complex data. This is done in the same way as regular reads - just the data
# returned is different.
try:
    value = IEasyUAClientExtension.ReadValue(client, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display basic information about what we have read.
print(value)


# We know that this node returns complex data, so we can type cast to UAGenericObject.
genericObject = value

# The actual data is in the GenericData property of the UAGenericObject.
#
# If we want to see the whole hierarchy of the received complex data, we can format it with the "V" (verbose)
# specifier. In the debugger, you can view the same by displaying the private DebugView property.
print()
print(String.Format('{0:V}', genericObject.GenericData))

# For processing the internals of the data, refer to examples for GenericData and DataType classes.

# .Int32Value
structuredData = genericObject.GenericData if isinstance(genericObject.GenericData, StructuredData) else None
fieldData = None if structuredData is None else structuredData.FieldData
fieldValue = None if fieldData is None else fieldData.get_Item('Int32Value')
primitiveData = fieldValue if isinstance(fieldValue, PrimitiveData) else None
int32Value = None if primitiveData is None else primitiveData.Value
print()
print('Int32Value: ', int32Value, sep='')

print()
print('Finished.')

##endregion Example
