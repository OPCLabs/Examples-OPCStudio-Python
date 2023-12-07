# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to write data into a section of an OPC UA file, using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from System.Text import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.OperationModel import *


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

# Open the file, write a section of it, and close it.
fileHandle = None
try:
    print('Opening file...')
    fileHandle = fileTransferClient.OpenFile(endpointDescriptor, fileNodeDescriptor,
                                             UAOpenFileModes.Read | UAOpenFileModes.Write)

    print('Writing file section...')
    data = Encoding.UTF8.GetBytes('TEXT FROM FILE TRANSFER CLIENT EXAMPLE. Demonstrates writing a section of a file. '
                                  '<<<')
    fileTransferClient.WriteFile(endpointDescriptor, fileNodeDescriptor, fileHandle, data)

    print('Closing file...')
    fileTransferClient.CloseFile(endpointDescriptor, fileNodeDescriptor, fileHandle)

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

finally:
    fileHandle and fileHandle.Dispose()

print()
print('Finished.')

##endregion Example
