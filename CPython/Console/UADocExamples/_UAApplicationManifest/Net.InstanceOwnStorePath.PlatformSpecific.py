# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example demonstrates how to place the client certificate in the platform-specific (Windows, Linux, ...)
# certificate store.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.OperationModel import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Set the application certificate store path, which determines the location of the client certificate.
# Note that this only works once in each host process.
EasyUAApplication.Instance.ApplicationParameters.ApplicationManifest.InstanceOwnStorePath = 'CurrentUser\\My'

# Do something - invoke an OPC read, to trigger creation of the certificate.
client = EasyUAClient()
try:
    value = IEasyUAClientExtension.ReadValue(client,
                                             endpointDescriptor,
                                             UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)

# The certificate will be located or created in the specified platform-specific certificate store.
# On Windows, when viewed by the certmgr.msc tool, it will be under
# Certificates - Current User -> Personal -> Certificates.

print('Finished.')

##endregion Example
