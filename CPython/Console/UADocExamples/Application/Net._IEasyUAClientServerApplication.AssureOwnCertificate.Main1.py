# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to assure presence of the own application certificate, and display its thumbprint.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.Application.Extensions import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Obtain the application interface.
application = EasyUAApplication.Instance

try:
    print('Assuring presence of the own application certificate...')
    created = IEasyUAClientServerApplicationExtension.AssureOwnCertificate(application)

    print('A new certificate has been created.' if created else 'An existing certificate has been found.')

    print()
    print('Finding the current application certificate...')
    pkiCertificate = IEasyUAClientServerApplicationExtension.FindOwnCertificate(application)

    print()
    print('The thumbprint of the current application certificate is: ',
          None if pkiCertificate is None else pkiCertificate.Thumbprint,
          sep='')
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
