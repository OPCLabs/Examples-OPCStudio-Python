# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to set the validity period of the application instance certificate.
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


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
    # or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
    # or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

print('Setting the validity period of the auto-generated instance certificate to 50 years (600 months)...')
EasyUAApplication.Instance.ApplicationParameters.InstanceCertificateGenerationParameters.ValidityPeriodInMonths = 600

print('Obtaining the application interface...')
client = EasyUAClient()
application = EasyUAApplication.Instance

try:
    print('Removing the current application instance certificate pack...')
    IEasyUAClientServerApplicationExtension.RemoveOwnCertificatePack(application, False) # mustExist=False

    print('Do something - invoke an OPC read, to trigger auto-generation of a new instance certificate...')
    IEasyUAClientExtension.ReadValue(client,
                                     endpointDescriptor, UANodeDescriptor("nsu=http://test.org/UA/Data/ ;i=10853"))

    print('Finding the current default application instance certificate...')
    instanceCertificate = IEasyUAClientServerApplicationExtension.FindOwnCertificate(application)

    if instanceCertificate is not None:
        print('Expiration date: ', instanceCertificate.NotAfter, sep='')
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
