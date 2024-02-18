# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to configure the OPC UA Complex Data plug-in to use a shared data type model provider.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *
from OpcLabs.EasyOpc.UA.Plugins.ComplexData import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# [ObjectsFolder]/Data.Static.Scalar.StructureValue
nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10239')


# We will create two instances of EasyUAClient class, and configure each of them to use the shared data type
# model provider.

# Configure the first client object.
client1 = EasyUAClient()
complexDataClientPluginParameters1 = (
    client1.InstanceParameters.PluginConfigurations.Find[UAComplexDataClientPluginParameters]())
assert complexDataClientPluginParameters1 is not None
complexDataClientPluginParameters1.IsolatedDataTypeModelProvider = False

# Configure the second client object.
client2 = EasyUAClient()
complexDataClientPluginParameters2 = (
    client1.InstanceParameters.PluginConfigurations.Find[UAComplexDataClientPluginParameters]())
assert complexDataClientPluginParameters2 is not None
complexDataClientPluginParameters1.IsolatedDataTypeModelProvider = False


# We will now read the same complex data node using the two client objects.
#
# There is no noticeable difference in the results from the default state in which the client objects are
# set to use per-instance data type model provider. But, with the shared data type model provider, the metadata
# obtained during the read on the first client object and cached inside the data type model provider are reused
# during the read on the second client object, making this and the subsequent operations more efficient.

# Read the complex data node using the first client.
try:
    value1 = IEasyUAClientExtension.ReadValue(client1, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()
print(value1)

# Read the complex data node using the second client.
try:
    value2 = IEasyUAClientExtension.ReadValue(client2, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()
print(value1)


print()
print('Finished.')

##endregion Example
