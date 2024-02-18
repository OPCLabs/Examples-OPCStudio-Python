# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to find server applications that meet the specified filters, using the global discovery client.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Discovery import *
from OpcLabs.EasyOpc.UA.Gds import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which GDS we will work with.
gdsEndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer')

# Instantiate the global discovery client object.
globalDiscoveryClient = EasyUAGlobalDiscoveryClient()

# Find all servers registered in the GDS.
try:
    _, _, serverOnNetworkArray = globalDiscoveryClient.QueryServers(
        gdsEndpointDescriptor,
        0,  # startingRecordId
        0,  # maximumRecordsToReturn
        '', # applicationName
        '', # applicationUriString
        '', # productUriString
        Array.Empty[String](),  # serverCapabilities
        DateTime(), # out lastCounterResetTime
        Array.Empty[UAServerOnNetwork]()) # out serverOnNetworkArray
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for serverOnNetwork in serverOnNetworkArray:
    print()
    print('Server name: ', serverOnNetwork.ServerName, sep='')
    print('Discovery URL string: ', serverOnNetwork.DiscoveryUrlString, sep='')
    print('Server capabilities: ', serverOnNetwork.ServerCapabilities, sep='')

print()
print('Finished.')

##endregion Example
