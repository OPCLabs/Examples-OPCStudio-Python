# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to browse for OPC UA files, using the file transfer client.
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

# Create two files, and then browse the directory that contains them.
try:
    # The file system node is a root directory of the file system.
    print('Getting file system...')
    fileSystemNodeDescriptor = IEasyUAFileTransferExtension.GetFileSystem(fileTransferClient,
                                                                          endpointDescriptor, objectDescriptor)

    fileName1 = 'MyFile1-' + str(random.randint(0, 999_999_999))
    print("Creating first file, '", fileName1, "'...", sep='')
    IEasyUAFileTransferExtension.CreateFile(fileTransferClient, endpointDescriptor, fileSystemNodeDescriptor, fileName1)

    fileName2 = 'MyFile2-' + str(random.randint(0, 999_999_999))
    print("Creating second file, '", fileName1, "'...", sep='')
    IEasyUAFileTransferExtension.CreateFile(fileTransferClient, endpointDescriptor, fileSystemNodeDescriptor, fileName2)

    print('Browsing for files...')
    fileNodeDescriptorDictionary = IEasyUAFileTransferExtension.BrowseFiles(fileTransferClient,
                                                                            endpointDescriptor,
                                                                            fileSystemNodeDescriptor)
    # If you want browse for directories, use the BrowseDirectories method instead.

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print()
for pair in fileNodeDescriptorDictionary:
    print(pair)

print()
print('Finished.')

##endregion Example
