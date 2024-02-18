# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to copy an OPC UA file, using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import random

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')
endpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(endpointDescriptor,'john', 'master')

# An object that aggregates an OPC UA file system.
objectDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files')

# Create a random number generator - will be used for file/directory names.
random = random.Random()

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

# Prevent prompt to trust the server certificate (INSECURE, used just for smooth example flow).
EasyUAClient.SharedParameters.EngineParameters.CertificateAcceptancePolicy.TrustEndpointUrlString(
    endpointDescriptor.UrlString)

# Create a file, and a directory. Then, copy the file into the directory.
try:
    # The file system node is a root directory of the file system.
    print('Getting file system...')
    fileSystemNodeDescriptor = IEasyUAFileTransferExtension.GetFileSystem(fileTransferClient,
                                                                          endpointDescriptor, objectDescriptor)

    fileName = 'MyFile-' + str(random.randint(0, 999_999_999))
    print("Creating file, '", fileName, "'...", sep='')
    fileNodeId = IEasyUAFileTransferExtension.CreateFile(fileTransferClient,
                                                         endpointDescriptor, fileSystemNodeDescriptor, fileName)
    print('Node Id of the file: ', fileNodeId, sep='')

    directoryName = 'MyDirectory-' + str(random.randint(0, 999_999_999))
    print("Creating directory, '", directoryName, "'...", sep='')
    directoryNodeId = fileTransferClient.CreateDirectory(endpointDescriptor,
                                                         fileSystemNodeDescriptor,
                                                         directoryName)
    print('Node Id of the directory: ', directoryNodeId, sep='')

    print('Copying the file...')
    IEasyUAFileTransferExtension.CopyFile(fileTransferClient,
                                          endpointDescriptor, fileSystemNodeDescriptor, fileNodeId, directoryNodeId)
    # If you want browse for directories, use the BrowseDirectories method instead.

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
