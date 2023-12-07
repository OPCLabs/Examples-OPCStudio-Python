# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to read different sections from an OPC UA file stream.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
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

streamReader = None
try:
    # Get a stream reader object that corresponds to an OPC UA file.
    print('Opening the file for reading...')

    # We know that the file contains text, so we read it using a stream reader. If the file content was
    # binary, you would process the stream according to the data format.
    streamReader = IEasyUAFileTransferExtension2.OpenStreamReader(fileTransferClient,
                                                                  endpointDescriptor,
                                                                  UANamedNodeDescriptor(fileNodeDescriptor))

    # The OPC UA stream reader object behaves like any other stream reader in .NET.

    # Read in the text from the file and display it line by line.
    print()
    print('Reading text lines...')
    i = 0
    while not streamReader.EndOfStream:
        line = streamReader.ReadLine()
        print('[', i, '] ', line, sep='')
        i = i + 1

# OPC UA errors encountered during opening of a UA file stream and operations on such stream are transformed
# to IOException-s.
except IOException as ioException:
    print('*** Failure: ' + ioException.GetBaseException().Message)
    exit()

finally:
    streamReader and streamReader.Dispose()

print()
print('Finished.')

##endregion Example
