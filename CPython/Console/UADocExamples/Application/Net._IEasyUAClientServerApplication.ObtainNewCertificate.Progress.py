# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to obtain a new application certificate from the certificate manager (GDS), and store it for subsequent
# usage, with progress reporting.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.Application.Extensions import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which GDS we will work with.
gdsEndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer')
gdsEndpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(gdsEndpointDescriptor,
                                                                           'appadmin', 'demo')

# Obtain the application interface.
application = EasyUAApplication.Instance

# Display which application we are about to work with.
applicationElement = IEasyUAClientServerApplicationExtension.GetApplicationElement(application)
print('Application URI string: ', applicationElement.ApplicationUriString, sep='')

# Obtain a new application certificate from the certificate manager (GDS), and store it for subsequent usage.
try:
    print('Obtaining new certificate...')
    certificate = IEasyUAClientServerApplicationExtension.ObtainNewCertificate(application,
        gdsEndpointDescriptor,
        Progress[String](Action[String](lambda s: print('Progress: ', s, sep=''))))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print()
print('Certificate: ', certificate, sep='')

print()
print('Finished.')

##endregion Example
