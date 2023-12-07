# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Shows how to open a file stream for reading, and read its content using a text reader object, using OPC UA file provider
# model.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.IO import *
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
streamReader = None
try:
    # Get a stream reader object that corresponds to an OPC UA file.
    print('Opening the file for reading...')

    # We know that the file contains text, so we read it using a stream reader. If the file content was
    # binary, you would process the stream according to the data format.
    streamReader = IFileInfoExtension.CreateStreamReader(fileInfo2)

    # Read in the text from the file and display it line by line.
    print()
    print('Reading text lines...')
    i = 0
    while not streamReader.EndOfStream:
        line = streamReader.ReadLine()
        print('[', i, '] ', line, sep='')
        i = i + 1

# Methods in the file provider model throw IOException and other exceptions, but not UAException.
except Exception as exception:
    print('*** Failure: ' + exception.GetBaseException().Message)
    exit()

finally:
    streamReader and streamReader.Dispose()

print()
print('Finished.')

##endregion Example
