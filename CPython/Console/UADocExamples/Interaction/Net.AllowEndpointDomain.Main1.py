# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how in a console application, the user is asked to allow a server instance certificate with
# mismatched domain name.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which server we will work with.
# Note that extra '.' at the end of the domain name. For the purpose of this example, it allows us to address
# the same domain, but cause a mismatch with what the names that are listed in the server instance certificate.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com.:51210/UA/SampleServer')

# Instantiate the client object.
client = EasyUAClient()
# Enforce the endpoint domain check.
client.Isolated = True
client.IsolatedParameters.SessionParameters.CheckEndpointDomain = True

try:
    # Obtain attribute data.
    # The component automatically triggers the necessary user interaction during the first operation.
    attributeData = IEasyUAClientExtension.Read(client,
                                                endpointDescriptor,
                                                UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('Value: ', attributeData.Value)
print('ServerTimestamp: ', attributeData.ServerTimestamp)
print('SourceTimestamp: ', attributeData.SourceTimestamp)
print('StatusCode: ', attributeData.StatusCode)

print()
print('Finished.')

##endregion Example
