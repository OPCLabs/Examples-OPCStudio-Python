# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# This example shows how to read 4 items from the device, and display their values, timestamps and qualities.
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


# Instantiate the client object.
client = EasyDAClient()

# DADataSource enumeration:
# Selects the data source for OPC reads (from device, from OPC cache, or dynamically determined).
# The data source (memory, OPC cache or OPC device) selection will be based on the desired value age and
# current status of data received from the server.

vtqResults = client.ReadMultipleItems(
    [
        DAReadItemArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Dynamic/Analog Types/Double'), DAReadParameters(DADataSource.Device)),
        DAReadItemArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Dynamic/Analog Types/Double[]'), DAReadParameters(DADataSource.Device)),
        DAReadItemArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Dynamic/Analog Types/Int'), DAReadParameters(DADataSource.Device)),
        DAReadItemArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Static/Analog Types/Int'), DAReadParameters(DADataSource.Device))
    ])

for i, vtqResult in enumerate(vtqResults):
    assert vtqResult is not None
    if vtqResult.Succeeded:
        print('vtqResults[', i, '].Vtq: ', vtqResult.Vtq, sep='')
    else:
        print('vtqResults[', i, '] *** Failure: ', vtqResult.ErrorMessageBrief, sep='')

# Example output:
#
#vtqResults[0].Vtq: 100 {Double} @2024-01-01T14:31:03.232; GoodNonspecific (192)
#vtqResults[1].Vtq: [3] {1000, 1000, 1000} {Double[]} @2024-01-01T14:31:03.232; GoodNonspecific (192)
#vtqResults[2].Vtq: 700 {Int32} @2024-01-01T14:31:03.232; GoodNonspecific (192)
#vtqResults[3].Vtq: 0 {Int32} @2024-01-01T14:31:03.232; GoodNonspecific (192)

##endregion Example
