# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to get OPC UA file properties (such as its size or writable status), using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.FileTransfer import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Unified Automation .NET based demo server (UaNETServer/UaServerNET.exe).
endpointDescriptor = UAEndpointDescriptor('opc.tcp://localhost:48030')

# A node that represents an instance of OPC UA FileType object.
fileNodeDescriptor = UANodeDescriptor('nsu=http://www.unifiedautomation.com/DemoServer/ ;s=Demo.Files.TextFile')

# Instantiate the file transfer client object.
fileTransferClient = EasyUAFileTransferClient()

# Get properties of a specified file.
try:
    print('Getting file properties...')
    fileProperties = IEasyUAFileTransferExtension.GetFileProperties(fileTransferClient,
                                                                    endpointDescriptor, fileNodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display result.
print()
print('MimeType: ', fileProperties.MimeType, sep='')
print('OpenCount: ', fileProperties.OpenCount, sep='')
print('Size: ', fileProperties.Size, sep='')
print('UserWritable: ', fileProperties.UserWritable, sep='')
print('Writable: ', fileProperties.Writable, sep='')
print('Timestamp: ', fileProperties.Timestamp, sep='')

print()
print('Finished.')

##endregion Example
