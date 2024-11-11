# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to read the full contents of an OPC UA file at once, using the file transfer client.
# Note: Consider using a higher-level abstraction, OPC UA file provider, instead.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Text import *
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

# Read in all contents from a specified file node.
try:
    print('Reading the whole file...')
    bytes = IEasyUAFileTransferExtension2.ReadAllBytes(fileTransferClient,
                                                       endpointDescriptor,
                                                       UANamedNodeDescriptor(fileNodeDescriptor))

# Beware that ReadAllFileBytes throws IOException and not UAException.
except IOException as ioException:
    print('*** Failure: ' + ioException.GetBaseException().Message)
    exit()

# Display result.
print()
# We know that the file contains text, so we convert the received data to a string. If the file contents was
# binary, you would process the data according to their format.
text = Encoding.UTF8.GetString(bytes)
print('File content:')
print(text)

print()
print('Finished.')

##endregion Example
