# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to get the OPC UA registration information for this application.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.Application.Extensions import *
from OpcLabs.EasyOpc.UA.Discovery import *


# Obtain the application interface.
application = EasyUAApplication.Instance

# Get the OPC UA registration information for this application.
applicationElement = IEasyUAClientServerApplicationExtension.GetApplicationElement(application)

# Display results.
print('Application element:')
print('  Application name: ', applicationElement.ApplicationName, sep='')
print('  Application type: ', Enum.Format(UAApplicationTypes, applicationElement.ApplicationType, 'G'), sep='')
print('  Application URI string: ', applicationElement.ApplicationUriString, sep='')
print('  Discovery URI strings: ', applicationElement.DiscoveryUriStrings, sep='')
print('  Product URI string: ', applicationElement.ProductUriString, sep='')

print()
print('Finished.')

##endregion Example
