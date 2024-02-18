# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to let the user browse for a host (computer) and an endpoint of an OPC-UA server residing on it.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.UA.Forms.Browsing import *


hostAndEndpointDialog = UAHostAndEndpointDialog()
hostAndEndpointDialog.EndpointDescriptor.Host = 'opcua.demo-this.com'

dialogResult = hostAndEndpointDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print('HostElement: ', hostAndEndpointDialog.HostElement, sep='')
print('DiscoveryElement: ', hostAndEndpointDialog.DiscoveryElement, sep='')

print('Finished.')

##endregion Example
