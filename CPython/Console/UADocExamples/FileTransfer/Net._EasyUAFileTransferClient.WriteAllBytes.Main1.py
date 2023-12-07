# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to write the full contents of an OPC UA file at once, using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Text import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.IO.Extensions import *
from OpcLabs.EasyOpc.UA.Navigation import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')
endpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(endpointDescriptor,'john', 'master')

# A node that represents an instance of OPC UA FileType object.
fileNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.TextFile')

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

# Prevent prompt to trust the server certificate (INSECURE, used just for smooth example flow).
EasyUAClient.SharedParameters.EngineParameters.CertificateAcceptancePolicy.TrustEndpointUrlString(
    endpointDescriptor.UrlString)

# Write all contents into a specified file node.
bytes = Encoding.UTF8.GetBytes('TEXT FROM FILE TRANSFER CLIENT EXAMPLE. Demonstrates writing the whole contents of a '
                               'file at once.')
try:
    print('Writing the whole file...')
    IEasyUAFileTransferExtension2.WriteAllBytes(fileTransferClient,
                                                endpointDescriptor,
                                                UANamedNodeDescriptor(fileNodeDescriptor),
                                                bytes)

    # Due to an issue in the server, the file might not be readable now, without server restart.
    print('Reading the data back...')
    data = IEasyUAFileTransferExtension2.ReadAllBytes(fileTransferClient,
                                                       endpointDescriptor,
                                                       UANamedNodeDescriptor(fileNodeDescriptor))
    print(Encoding.UTF8.GetString(data))

# Beware that ReadAllFileBytes throws IOException and not UAException.
except IOException as ioException:
    print('*** Failure: ' + ioException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
