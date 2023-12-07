# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to completely turn off interaction in a console application.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Engine import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Do not implicitly trust any endpoint URLs. We want the user be asked explicitly.
EasyUAClient.SharedParameters.EngineParameters.CertificateAcceptancePolicy.TrustedEndpointUrlStrings.Clear()

# Completely disable the console interaction.
EasyUAClient.SharedParameters.PluginSetups.FindName('UAConsoleInteraction').Enabled = False

# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# Require secure connection, in order to enforce the certificate check.
endpointDescriptor.EndpointSelectionPolicy = UAEndpointSelectionPolicy(UAMessageSecurityModes.Secure)

# Instantiate the client object.
client = EasyUAClient()

try:
    # Obtain attribute data.
    # The operation will fail, unless you set up mutual trust using certificate stores.
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
