# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain information about OPC UA servers from the Global Discovery Server (GDS).
# The result is hierarchical, i.e. each server is returned in one element, and the element contains all its discovery
# URLs.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Discovery import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Instantiate the client object.
client = EasyUAClient()

# Obtain collection of application elements.
try:
    discoveryElementCollection = IEasyUAClientExtension.DiscoverGlobalServers(client,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer'),
        False) # flat=False
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for discoveryElement in discoveryElementCollection:
    print()
    print('Server name: ', discoveryElement.ServerName, sep='')
    print('Discovery URI strings:')
    for discoveryUriString in discoveryElement.DiscoveryUriStrings:
        print('  ', discoveryUriString, sep='')
    print('Server capabilities: ', discoveryElement.ServerCapabilities, sep='')
    print('Application URI string: ', discoveryElement.ApplicationUriString, sep='')
    print('Product URI string: ', discoveryElement.ProductUriString, sep='')

print()
print('Finished.')

##endregion Example
