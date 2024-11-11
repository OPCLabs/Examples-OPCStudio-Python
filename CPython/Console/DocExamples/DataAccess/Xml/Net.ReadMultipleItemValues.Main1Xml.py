# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how to read values of 4 items at once, and display them.
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

valueResults = IEasyDAClientExtension.ReadMultipleItemValues(client,
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    [
        DAItemDescriptor('Dynamic/Analog Types/Double'),
        DAItemDescriptor('Dynamic/Analog Types/Double[]'),
        DAItemDescriptor('Dynamic/Analog Types/Int'),
        DAItemDescriptor('Static/Analog Types/Int')
    ])

for i, valueResult in enumerate(valueResults):
    assert valueResult is not None
    if valueResult.Succeeded:
        print('valueResults[', i, '].Value: ', valueResult.Value, sep='')
    else:
        print('valueResults[', i, '] *** Failure: ', valueResult.ErrorMessageBrief, sep='')


# Example output:
#
#valueResults[0].Value: 0.00125125888851588
#valueResults[1].Value: System.Double[]
#valueResults[2].Value: -0.993968485238202
#valueResults[3].Value: 0

##endregion Example
