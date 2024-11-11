# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to create and delete OPC UA directories, using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
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

# Create two directories, and one nested directory, and delete the first one.
try:
    # The file system node is a root directory of the file system.
    print('Getting file system...')
    fileSystemNodeDescriptor = IEasyUAFileTransferExtension.GetFileSystem(fileTransferClient,
                                                                          endpointDescriptor, objectDescriptor)

    directoryName1 = 'MyDirectory1-' + str(random.randint(0, 999_999_999))
    print("Creating first directory, '", directoryName1, "'...", sep='')
    directoryNodeId1 = fileTransferClient.CreateDirectory(endpointDescriptor,
                                                          fileSystemNodeDescriptor,
                                                          directoryName1)
    print('Node Id of the first directory: ', directoryNodeId1, sep='')

    directoryName2 = 'MyDirectory2-' + str(random.randint(0, 999_999_999))
    print("Creating second directory, '", directoryName2, "'...", sep='')
    directoryNodeId2 = fileTransferClient.CreateDirectory(endpointDescriptor,
                                                          fileSystemNodeDescriptor,
                                                          directoryName2)
    print('Node Id of the second directory: ', directoryNodeId1, sep='')

    nestedDirectoryName = 'MyDirectory3-' + str(random.randint(0, 999_999_999))
    print("Creating nested directory, '", nestedDirectoryName, "'...", sep='')
    # Note how directoryNodeId2 (a parent directory) is passed as the 2nd argument to the CreateDirectory method.
    nestedDirectoryNodeId = fileTransferClient.CreateDirectory(endpointDescriptor,
                                                               UANodeDescriptor(directoryNodeId2),
                                                               nestedDirectoryName)
    print('Node Id of the nested directory: ', nestedDirectoryNodeId, sep='')

    # At this moment, the directory structure we have created looks like this:
    # * MyDirectory1
    # * MyDirectory2
    # * * MyDirectory3

    print('Deleting the first directory...')
    IEasyUAFileTransferExtension.DeleteDirectory(fileTransferClient,
                                                 endpointDescriptor, fileSystemNodeDescriptor, directoryName1)

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
