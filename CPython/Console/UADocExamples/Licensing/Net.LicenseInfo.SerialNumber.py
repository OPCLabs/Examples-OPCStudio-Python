# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to obtain the serial number of the active license, and determine whether it is a stock demo or trial license.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *


# Instantiate the client object.
client = EasyUAClient()

# Obtain the serial number from the license info.
serialNumber = client.LicenseInfo.get_Item('Multipurpose.SerialNumber')

# Display the serial number.
print('SerialNumber: ', serialNumber, sep='')

# Determine whether we are running as demo or trial.
if (1111110000 <= serialNumber) and (serialNumber <= 1111119999):
    print('This is a stock demo or trial license.')
else:
    print('This is not a stock demo or trial license.')

print()
print('Finished.')

##endregion Example
