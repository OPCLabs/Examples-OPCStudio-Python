# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to write data into a section of an OPC UA file, using the file provider model.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from System.IO import *
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

# Open the file, write a section of it, and close it.
stream = None
try:
    print('Opening file...')
    stream = writableFileInfo.CreateWriteStream(FileMode.Open, FileAccess.ReadWrite)

    print('Writing file section...')
    data = Encoding.UTF8.GetBytes('TEXT FROM FILE TRANSFER CLIENT EXAMPLE. Demonstrates writing a section of a file. '
                                  '<<<')
    stream.Write(data, 0, data.Length)

    print('Closing file...')
    # Disposing of the stream (in the 'finally' block) closes the file.

# Methods in the file provider model throw IOException and other exceptions, but not UAException.
except Exception as exception:
    print('*** Failure: ' + exception.GetBaseException().Message)
    exit()

finally:
    stream and stream.Dispose()

print()
print('Finished.')

##endregion Example
