# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# Parses an absolute  OPC-UA browse path and displays its starting node and elements.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.Navigation import *
from OpcLabs.EasyOpc.UA.Navigation.Parsing import *


browsePathParser = UABrowsePathParser()
try:
    browsePath = browsePathParser.Parse('[ObjectsFolder]/Data/Static/UserScalar')
except UABrowsePathFormatException as browsePathFormatException:
    print('*** Failure: ' + browsePathFormatException.GetBaseException().Message)
    exit()

# Display results.
print('StartingNodeId: ', browsePath.StartingNodeId, sep='')

print()
for browsePathElement in browsePath.Elements:
    print(browsePathElement)

print()
print('Finished.')

##endregion Example
