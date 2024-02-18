# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to create an application registration in the GDS, assigning it a new application ID.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
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

# Create an application registration in the GDS, assigning it a new application ID.
try:
    print('Registering to GDS...')
    applicationId = application.RegisterToGds(gdsEndpointDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('Application ID: ', applicationId, sep='')

print()
print('Finished.')

##endregion Example
