# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to retrieve all sub-types of a given data type, recursively.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Retrieve all sub-types of the 'Structure' data type.
valueResult = IEasyUAClientExtension2.RetrieveAllDataTypes(client,
                                                           endpointDescriptor,
                                                           UANodeDescriptor(UADataTypeIds.Structure))
# Check if the operation succeeded. Use the ThrowIfFailed method instead if you want exception be thrown.
if not valueResult.Succeeded:
    print('*** Failure: ', valueResult.ErrorMessageBrief, sep='')
    exit()

# Display results. Note that all node descriptors have node IDs in them; but the default display format shows
# the browse paths, which are more readable, when they are available.
for nodeDescriptor in valueResult.Value:
    print(nodeDescriptor)

print()
print('Finished.')

##endregion Example
