# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to let the user browse for multiple OPC-UA nodes.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.UA.Forms.Browsing import *


browseDialog = UABrowseDialog()
browseDialog.InputsOutputs.CurrentNodeDescriptor.EndpointDescriptor.Host = "opcua.demo-this.com"
browseDialog.Mode.AnchorElementType = UAElementType.Host
browseDialog.Mode.MultiSelect = True

dialogResult = browseDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
selectionElements = browseDialog.Outputs.SelectionElements
for i, selectionElement in enumerate(selectionElements):
    print('SelectionElements[', i, '].NodeElement: ', selectionElement.NodeElement, sep='')

print()
print('Finished.')

##endregion Example
