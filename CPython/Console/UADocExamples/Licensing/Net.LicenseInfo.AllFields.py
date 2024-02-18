# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to display all fields of the available license(s).
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *


# Instantiate the client object.
client = EasyUAClient()

# Obtain the license info.
licenseInfo = client.LicenseInfo

# Display all elements.
for pair in licenseInfo:
    print(pair.Key, ': ', pair.Value, sep='')

print()
print('Finished.')

##endregion Example
