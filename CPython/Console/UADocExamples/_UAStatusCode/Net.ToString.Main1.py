# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how the OPC UA status codes are formatted to a string containing their symbolic name.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *


internalValueArray = [0, 0x80010000, 2147614720, 0x80340000]

for internalValue in internalValueArray:
    print(internalValue, ': ', UAStatusCode(internalValue), sep='')

print()
print('Finished.')


# Example output:
# 0: Good
# 2147549184: BadUnexpectedError
# 2147614720: BadInternalError
# 2150891520: BadNodeIdUnknown
#
# Finished.

##endregion Example
