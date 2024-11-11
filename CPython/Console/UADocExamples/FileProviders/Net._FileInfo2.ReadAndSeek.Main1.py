# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to read different sections from an OPC UA file, using the file provider model.
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

# Open the file, read two separate sections of it, and close it.
stream = None
try:
    print('Opening file...')
    stream = fileInfo2.CreateReadStream()

    print('Reading first section of a stream...')
    buffer1 = Array.CreateInstance(Byte, 16)
    bytesRead1, _ = stream.Read(buffer1, 0, buffer1.Length)
    print(bytesRead1, ' bytes read, buffer: ', BitConverter.ToString(buffer1), sep='')

    print('Reading second section of a stream...')
    buffer2 = Array.CreateInstance(Byte, 10)
    bytesRead2, _ = stream.Read(buffer2, 0, buffer2.Length)
    print(bytesRead2, ' bytes read, buffer: ', BitConverter.ToString(buffer2), sep='')

    print('Seeking...')
    stream.Seek(100, SeekOrigin.Begin)

    print('Reading third section of a stream...')
    buffer3 = Array.CreateInstance(Byte, 20)
    bytesRead3, _ = stream.Read(buffer3, 0, buffer3.Length)
    print(bytesRead3, ' bytes read, buffer: ', BitConverter.ToString(buffer3), sep='')

# Methods in the file provider model throw IOException and other exceptions, but not UAException.
except Exception as exception:
    print('*** Failure: ' + exception.GetBaseException().Message)
    exit()

finally:
    stream and stream.Dispose()

print()
print('Finished.')

##endregion Example
