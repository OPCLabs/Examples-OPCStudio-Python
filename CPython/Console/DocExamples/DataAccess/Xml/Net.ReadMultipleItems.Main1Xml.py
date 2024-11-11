# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how to read 4 items from an OPC XML-DA server at once, and display their values, timestamps
# and qualities.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

#
vtqResultArray = IEasyDAClientExtension.ReadMultipleItems(client,
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    [
        DAItemDescriptor('Dynamic/Analog Types/Double'),
        DAItemDescriptor('Dynamic/Analog Types/Double[]'),
        DAItemDescriptor('Dynamic/Analog Types/Int'),
        DAItemDescriptor('SomeUnknownItem')
    ])

for i, vtqResult in enumerate(vtqResultArray):
    assert vtqResult is not None
    if vtqResult.Succeeded:
        print('vtqResultArray[', i, '].Vtq: ', vtqResult.Vtq, sep='')
    else:
        print('vtqResultArray[', i, '] *** Failure: ', vtqResult.ErrorMessageBrief, sep='')

##endregion Example
