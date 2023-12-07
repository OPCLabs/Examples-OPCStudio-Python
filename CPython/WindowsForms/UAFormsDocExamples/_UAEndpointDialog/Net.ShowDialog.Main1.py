# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for an OPC-UA server endpoint.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.UA.Forms.Browsing import *


endpointDialog = UAEndpointDialog()
endpointDialog.DiscoveryHost = 'opcua.demo-this.com'

dialogResult = endpointDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print(endpointDialog.DiscoveryElement)

print('Finished.')

##endregion Example
