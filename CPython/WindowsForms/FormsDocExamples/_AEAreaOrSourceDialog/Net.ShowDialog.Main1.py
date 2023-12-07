# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for OPC Alarms&Events areas or sources.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.AlarmsAndEvents.Forms.Browsing import *


areaOrSourceDialog = AEAreaOrSourceDialog()
areaOrSourceDialog.ServerDescriptor.ServerClass = "OPCLabs.KitEventServer.2"

dialogResult = areaOrSourceDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print()
for nodeElement in areaOrSourceDialog.NodeElements:
    print(nodeElement)

##endregion Example
