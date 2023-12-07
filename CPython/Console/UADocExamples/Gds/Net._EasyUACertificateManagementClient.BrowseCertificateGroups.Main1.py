# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to browse and display the certificate groups available in the Certificate Manager.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Gds import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which GDS we will work with.
gdsEndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer')

# Instantiate the certificate management client object.
certificateManagementClient = EasyUACertificateManagementClient()

# Browse the certificate groups available in the GDS.
try:
    certificateGroupElementCollection = certificateManagementClient.BrowseCertificateGroups(gdsEndpointDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
for certificateGroupElement in certificateGroupElementCollection:
    print(certificateGroupElement)

print()
print('Finished.')

##endregion Example
