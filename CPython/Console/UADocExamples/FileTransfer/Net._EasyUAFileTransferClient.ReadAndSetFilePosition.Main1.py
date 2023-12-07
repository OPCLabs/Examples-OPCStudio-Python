# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to read different sections from an OPC UA file, using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')

# A node that represents an instance of OPC UA FileType object.
fileNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.TextFile')

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

# Open the file, read two separate sections of it, and close it.
fileHandle = None
try:
    print('Opening file...')
    fileHandle = fileTransferClient.OpenFile(endpointDescriptor, fileNodeDescriptor, UAOpenFileModes.Read)

    print('Reading first file section...')
    bytes1 = fileTransferClient.ReadFile(endpointDescriptor, fileNodeDescriptor, fileHandle, 16)    # length
    print('First section: ', BitConverter.ToString(bytes1), sep='')

    print('Reading second file section...')
    bytes2 = fileTransferClient.ReadFile(endpointDescriptor, fileNodeDescriptor, fileHandle, 10)    # length
    print('Second section: ', BitConverter.ToString(bytes2), sep='')

    print('Setting file position...')
    fileTransferClient.SetFilePosition(endpointDescriptor, fileNodeDescriptor, fileHandle, 100) # position

    print('Reading third file section...')
    bytes3 = fileTransferClient.ReadFile(endpointDescriptor, fileNodeDescriptor, fileHandle, 20)    # length
    print('Third section: ', BitConverter.ToString(bytes3), sep='')

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
