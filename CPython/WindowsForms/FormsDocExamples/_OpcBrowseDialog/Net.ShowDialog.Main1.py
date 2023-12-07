# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for an OPC Data Access node in a dialog.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.Forms.Browsing import *


browseDialog = OpcBrowseDialog()

dialogResult = browseDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print('DANodeElement: ', browseDialog.Outputs.CurrentNodeElement.DANodeElement, sep='')

##endregion Example
