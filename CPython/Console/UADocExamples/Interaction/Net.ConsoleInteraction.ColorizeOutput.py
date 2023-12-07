# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to configure the OPC UA Console Interaction plug-in by turning off the output colorization.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.Console.Interaction import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Engine import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Configure the shared plug-in.

# Find the parameters object of the plug-in.
consoleInteractionPluginParameters = EasyUAClient.SharedParameters.PluginConfigurations.Find[ConsoleInteractionParameters]()
assert consoleInteractionPluginParameters is not None
# Change the parameter.
consoleInteractionPluginParameters.ColorizeOutput = False


# Do not implicitly trust any endpoint URLs. We want the user be asked explicitly.
EasyUAClient.SharedParameters.EngineParameters.CertificateAcceptancePolicy.TrustedEndpointUrlStrings.Clear()

# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# Require secure connection, in order to enforce the certificate check.
endpointDescriptor.EndpointSelectionPolicy = UAEndpointSelectionPolicy(UAMessageSecurityModes.Secure)

# Instantiate the client object.
client = EasyUAClient()

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
