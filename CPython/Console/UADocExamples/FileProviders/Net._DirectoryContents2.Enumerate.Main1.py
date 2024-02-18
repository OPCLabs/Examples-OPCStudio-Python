# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to browse for OPC UA files and directories, using the file provider model.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import random

# Import .NET namespaces.
from System import *
from OpcLabs.BaseLib.Extensions.FileProviders import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Extensions import *
from OpcLabs.EasyOpc.UA.FileTransfer import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')
endpointDescriptor = UAEndpointDescriptorExtension.WithUserNameIdentity(endpointDescriptor,'john', 'master')

# A node that represents an OPC UA file system (a root directory).
fileSystemNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.FileSystem')

# Create a random number generator - will be used for file/directory names.
random = random.Random()

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

# Prevent prompt to trust the server certificate (INSECURE, used just for smooth example flow).
EasyUAClient.SharedParameters.EngineParameters.CertificateAcceptancePolicy.TrustEndpointUrlString(
    endpointDescriptor.UrlString)

print('Getting writable file provider...')
writableFileProvider = IEasyUAFileTransferExtension.GetWritableFileProvider(fileTransferClient,
                                                                            endpointDescriptor,
                                                                            fileSystemNodeDescriptor)
# From this point onwards, the code is independent of the concrete realization of the file provider, and would
# be identical e.g. for files in the physical file system, if the corresponding file provider was used.

# Create two files, and then browse the directory that contains them.
try:
    fileName1 = 'MyFile1-' + str(random.randint(0, 999_999_999))
    print("Creating first file, '", fileName1, "'...", sep='')
    writableFileInfo1 = writableFileProvider.GetWritableFileInfo(fileName1)
    IWritableFileInfoExtension.WriteAllBytes(writableFileInfo1, Array.Empty[Byte]())

    fileName2 = 'MyFile2-' + str(random.randint(0, 999_999_999))
    print("Creating second file, '", fileName2, "'...", sep='')
    writableFileInfo2 = writableFileProvider.GetWritableFileInfo(fileName2)
    IWritableFileInfoExtension.WriteAllBytes(writableFileInfo2, Array.Empty[Byte]())

    print('Browsing for files...')
    directoryContents2 = writableFileProvider.GetDirectoryContents2(None)
    for fileInfo2 in directoryContents2:
        print(fileInfo2)
    # You can distinguish between files and directories using the IFileInfo.IsDirectory property.

# Methods in the file provider model throw IOException and other exceptions, but not UAException.
except Exception as exception:
    print('*** Failure: ' + exception.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
