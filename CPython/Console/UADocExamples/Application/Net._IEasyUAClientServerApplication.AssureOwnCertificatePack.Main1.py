# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to assure presence of the own application certificate pack, and display default application certificate 
# thumbprint.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
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
    print('Assuring presence of the own application certificate pack...')
    created = IEasyUAClientServerApplicationExtension.AssureOwnCertificatePack(application)

    print('A new certificate pack has been created.' if created else 'An existing certificate pack has been found.')

    print()
    print('Finding the current default application certificate...')
    pkiCertificate = IEasyUAClientServerApplicationExtension.FindOwnCertificate(application)

    print()
    print('The thumbprint of the current default application certificate is: ',
          None if pkiCertificate is None else pkiCertificate.Thumbprint,
          sep='')
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
