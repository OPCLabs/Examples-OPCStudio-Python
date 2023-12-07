# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Parses a relative OPC-UA browse path and displays its elements.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Navigation import *
from OpcLabs.EasyOpc.UA.Navigation.Parsing import *


browsePathParser = UABrowsePathParser()
try:
    browsePathElements = browsePathParser.ParseRelative('/Data.Dynamic.Scalar.CycleComplete')
except UABrowsePathFormatException as browsePathFormatException:
    print('*** Failure: ' + browsePathFormatException.GetBaseException().Message)
    exit()

# Display results.
for browsePathElement in browsePathElements:
    print(browsePathElement)

print()
print('Finished.')

##endregion Example
