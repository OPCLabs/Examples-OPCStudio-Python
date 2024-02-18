# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to let the user browse for an OPC-UA data node (a Data Variable or a Property).
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.UA.Forms.Browsing import *


dataDialog = UADataDialog()
dataDialog.EndpointDescriptor.UrlString = 'opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'
dataDialog.UserPickEndpoint = True

dialogResult = dataDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print('EndpointDescriptor: ', dataDialog.EndpointDescriptor, sep='')
print('NodeElement: ', dataDialog.NodeElement, sep='')

print('Finished.')

##endregion Example
