# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to disable and enable the OPC UA Complex Data plug-in.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# [ObjectsFolder]/Data.Static.Scalar.StructureValue
nodeDescriptor = UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10239')


# We will explicitly disable the Complex Data plug-in, and read a node which returns complex data. We will
# receive an object of type UAExtensionObject, which contains the encoded data in its binary form. In this
# form, the data cannot be easily further processed by your application.
#
# Disabling the Complex Data plug-in may be useful e.g. for licensing reasons (when the product edition you
# have does not support the Complex Data plug-in, and you want to avoid the associated error), or for
# performance reasons (if you do not need the internal content of the value, for example if your code just
# needs to take the value read, and write it elsewhere).

client1 = EasyUAClient()
client1.InstanceParameters.PluginSetups.FindName('UAComplexDataClient').Enabled = False

try:
    value1 = IEasyUAClientExtension.ReadValue(client1, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()
print(value1)


# Now we will read the same value, but with the Complex Data plug-in enabled. This time we will receive an
# object of type UAGenericObject, which contains the data in the decoded form, accessible for further
# processing by your application.
#
# Note that it is not necessary to explicitly enable the Complex Data plug-in like this, because it is enabled
# by default.

client2 = EasyUAClient()
client2.InstanceParameters.PluginSetups.FindName('UAComplexDataClient').Enabled = True

try:
    value2 = IEasyUAClientExtension.ReadValue(client2, endpointDescriptor, nodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()
print(value2)

print()
print('Finished.')

##endregion Example
