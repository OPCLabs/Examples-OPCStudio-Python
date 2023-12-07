# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to obtain application URLs of all OPC Unified Architecture servers on the specified host.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Instantiate the client object.
client = EasyUAClient()

# Obtain collection of server elements.
try:
    discoveryElementCollection = IEasyUAClientExtension.DiscoverLocalServers(client, 'opcua.demo-this.com')
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for discoveryElement in discoveryElementCollection:
    print('DiscoveryElementCollection["', discoveryElement.DiscoveryUriString, '"].ApplicationUriString: ', 
          discoveryElement.ApplicationUriString, sep='')

##endregion Example
