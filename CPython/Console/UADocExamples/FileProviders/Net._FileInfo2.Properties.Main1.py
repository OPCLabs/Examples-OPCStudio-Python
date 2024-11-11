# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to get OPC UA file properties (such as its size or last modified time), using the file provider model.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib.Extensions.FileProviders import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.Navigation import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')

# A node that represents an instance of OPC UA FileType object.
fileNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.TextFile')

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

print('Getting file info......')
fileInfo2 = IEasyUAFileTransferExtension.GetFileInfo2(fileTransferClient,
                                                      endpointDescriptor,
                                                      UANamedNodeDescriptor(fileNodeDescriptor))
# From this point onwards, the code is independent of the concrete realization of the file provider, and would
# be identical e.g. for files in the physical file system, if the corresponding file provider was used.

# Get properties of a specified file.
try:
    # Display result.
    print()
    print('Exists: ', fileInfo2.Exists, sep='')
    print('IsDirectory: ', fileInfo2.IsDirectory, sep='')
    print('LastModified: ', fileInfo2.LastModified, sep='')
    print('Length: ', fileInfo2.Length, sep='')
    print('Name: ', fileInfo2.Name, sep='')
    print('PhysicalPath: ', fileInfo2.PhysicalPath, sep='')

# Methods in the file provider model throw IOException and other exceptions, but not UAException.
except Exception as exception:
    print('*** Failure: ' + exception.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
