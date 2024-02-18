# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to write the full contents of an OPC UA file at once, using the file provider model.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from System.Text import *
from OpcLabs.BaseLib.Extensions.FileProviders import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.Navigation import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')

# A node that represents an OPC UA file system (a root directory).
fileNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.TextFile')

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

print('Getting writable file info...')
writableFileInfo = IEasyUAFileTransferExtension.GetWritableFileInfo(fileTransferClient,
                                                                    endpointDescriptor,
                                                                    UANamedNodeDescriptor(fileNodeDescriptor))
# From this point onwards, the code is independent of the concrete realization of the file provider, and would
# be identical e.g. for files in the physical file system, if the corresponding file provider was used.

# Write all contents into a specified file node.
bytes = Encoding.UTF8.GetBytes('TEXT FROM FILE TRANSFER CLIENT EXAMPLE. Demonstrates writing the whole contents of a '
                               'file at once.')
try:
    print('Writing the whole file...')
    IWritableFileInfoExtension.WriteAllBytes(writableFileInfo, bytes)

    # Due to an issue in the server, the file might not be readable now, without server restart.
    print('Reading the data back...')
    data = IFileInfoExtension.ReadAllBytes(writableFileInfo)
    print(Encoding.UTF8.GetString(data))

# Methods in the file provider model throw IOException and other exceptions, but not UAException.
except Exception as exception:
    print('*** Failure: ' + exception.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
