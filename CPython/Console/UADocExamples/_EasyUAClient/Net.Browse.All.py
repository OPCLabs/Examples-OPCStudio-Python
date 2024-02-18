# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to obtain references of all kinds to nodes of all classes, from the "Server" node in the address space.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Collections.Generic import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

# Obtain nodes under "Server" node.
try:
    referenceTypeIdList = List[UANodeId]()
    referenceTypeIdList.Add(UAReferenceTypeIds.References)
    nodeElementCollection = IEasyUAClientExtension.Browse(client,
         endpointDescriptor,
         UANodeDescriptor(UAObjectIds.Server),
         UABrowseParameters(UANodeClass.All, referenceTypeIdList))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for nodeElement in nodeElementCollection:
    assert nodeElement is not None
    print()
    print('nodeElement.DisplayName: ', nodeElement.DisplayName, sep='')
    print('nodeElement.NodeId: ', nodeElement.NodeId, sep='')
    print('nodeElement.NodeId.ExpandedText: ', nodeElement.NodeId.ExpandedText, sep='')

print()
print('Finished.')

##endregion Example
