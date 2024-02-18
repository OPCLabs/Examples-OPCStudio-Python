# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to let the user browse for an OPC "Classic" server.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System.Windows.Forms import *
from OpcLabs.EasyOpc.Forms.Browsing import *


serverDialog = OpcServerDialog()
#serverDialog.Location = ''

dialogResult = serverDialog.ShowDialog()
print(dialogResult)
if dialogResult != DialogResult.OK:
    exit()

# Display results.
print('ServerElement: ', serverDialog.ServerElement, sep='')

##endregion Example
