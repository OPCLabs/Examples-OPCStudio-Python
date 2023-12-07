# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to read different sections from an OPC UA file stream.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from System.IO import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.IO.Extensions import *
from OpcLabs.EasyOpc.UA.Navigation import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')

# A node that represents an instance of OPC UA FileType object.
fileNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.TextFile')

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

stream = None
try:
    # Get a stream object that corresponds to an OPC UA file.
    print('Opening the file for reading...')
    stream = IEasyUAFileTransferExtension2.OpenStream(fileTransferClient,
                                                      endpointDescriptor,
                                                      UANamedNodeDescriptor(fileNodeDescriptor))

    # The OPC UA file stream object behaves like any other stream in .NET.

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

# OPC UA errors encountered during opening of a UA file stream and operations on such stream are transformed
# to IOException-s.
except IOException as ioException:
    print('*** Failure: ' + ioException.GetBaseException().Message)
    exit()

finally:
    stream and stream.Dispose()

print()
print('Finished.')

##endregion Example
