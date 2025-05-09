# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain application URLs of all OPC Unified Architecture servers, using specified discovery
# URI strings.
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


discoveryUriStrings = [
    'opc.tcp://opcua.demo-this.com:4840/UADiscovery',
    'http://opcua.demo-this.com/UADiscovery/Default.svc',
    'http://opcua.demo-this.com:52601/UADiscovery'
]

# Instantiate the client object.
client = EasyUAClient()

# Obtain collection of application elements.
try:
    discoveryElementCollection = IEasyUAClientExtension.FindLocalApplications(client,
        discoveryUriStrings, UAApplicationTypes.Server)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for discoveryElement in discoveryElementCollection:
    print('DiscoveryElementCollection["', discoveryElement.DiscoveryUriString, '"].ApplicationUriString: ',
          discoveryElement.ApplicationUriString, sep='')

##endregion Example
