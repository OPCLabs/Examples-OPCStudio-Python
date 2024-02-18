# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to unregister all clients from a GDS.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Discovery import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.Gds import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which GDS we will work with.
gdsEndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:58810/GlobalDiscoveryServer')
gdsEndpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(gdsEndpointDescriptor,
                                                                           'appadmin', 'demo')

# Instantiate the global discovery client object.
globalDiscoveryClient = EasyUAGlobalDiscoveryClient()

# Find application IDs of all client applications registered in the GDS.
clientApplicationIds = set()
try:
    _, _, _, applicationDescriptionArray = globalDiscoveryClient.QueryApplications(
        gdsEndpointDescriptor,
        0,  # startingRecordId
        0,  # maximumRecordsToReturn
        '', # applicationName
        '', # applicationUriString
        UAApplicationTypes.Client, # applicationTypes
        '', # productUriString
        Array.Empty[String](),  # serverCapabilities
        DateTime(), # out lastCounterResetTime
        0,  # out nextRecordId
        Array.Empty[UAApplicationDescription]()) # out applications

    for applicationDescription in applicationDescriptionArray:
        applicationRecordArray = globalDiscoveryClient.FindApplications(
            gdsEndpointDescriptor,
            applicationDescription.ApplicationUriString)
        for applicationRecord in applicationRecordArray:
            clientApplicationIds.add(applicationRecord.ApplicationId)

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Unregister all client applications found.
for applicationId in clientApplicationIds:
    print()
    print('Application ID: ', applicationId, sep='')

    try:
        globalDiscoveryClient.UnregisterApplication(gdsEndpointDescriptor, applicationId)
    except UAException as uaException:
        print('*** Failure: ' + uaException.GetBaseException().Message)
        continue
    print('Application unregistered.')

print()
print('Finished.')

##endregion Example
