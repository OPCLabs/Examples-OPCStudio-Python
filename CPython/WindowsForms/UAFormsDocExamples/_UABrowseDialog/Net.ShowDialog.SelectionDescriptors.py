# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how the current node and selected nodes can be persisted between dialog invocations.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Forms.Browsing import *


# The variables that persist the current and selected nodes.
currentNodeDescriptor = UABrowseNodeDescriptor()
selectionDescriptors = UABrowseNodeDescriptorCollection()

# The initial current node (optional).

currentNodeDescriptor.EndpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')

# Repeatedly show the dialog until the user cancels it.

while True:
    browseDialog = UABrowseDialog()
    browseDialog.Mode.MultiSelect = True

    # Set the dialog inputs from the persistence variables.

    browseDialog.InputsOutputs.CurrentNodeDescriptor = currentNodeDescriptor
    browseDialog.InputsOutputs.SelectionDescriptors.Clear()
    for browseNodeDescriptor in selectionDescriptors:
        browseDialog.InputsOutputs.SelectionDescriptors.Add(browseNodeDescriptor)

    dialogResult = browseDialog.ShowDialog()
    print(dialogResult)
    if dialogResult != DialogResult.OK:
        break

    # Update the persistence variables with the dialog output.

    currentNodeDescriptor = browseDialog.InputsOutputs.CurrentNodeDescriptor
    selectionDescriptors.Clear()
    for browseNodeDescriptor in browseDialog.InputsOutputs.SelectionDescriptors:
        selectionDescriptors.Add(browseNodeDescriptor)

print('Finished.')

##endregion Example
