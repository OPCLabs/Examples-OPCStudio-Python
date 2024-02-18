# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to check if an application needs to update its certificate.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.Gds import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which GDS we will work with.
gdsEndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer')
gdsEndpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(gdsEndpointDescriptor,
                                                                           'appadmin', 'demo')

# Register our client application with the GDS, so that we obtain an application ID that we need later.
# Obtain the application interface.
application = EasyUAApplication.Instance
try:
    print('Registering to GDS...')
    applicationId = application.RegisterToGds(gdsEndpointDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()
print('Application ID: ', applicationId, sep='')

# Instantiate the certificate management client object.
certificateManagementClient = EasyUACertificateManagementClient()

# Check if the application needs to update its certificate.
try:
    updateRequired = certificateManagementClient.GetCertificateStatus(gdsEndpointDescriptor,
                                                                      applicationId,
                                                                      UANodeId.Null,    # certificateGroupId
                                                                      UANodeId.Null)    # certificateTypeId
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('Update required: ', updateRequired, sep='')

print()
print('Finished.')

##endregion Example
