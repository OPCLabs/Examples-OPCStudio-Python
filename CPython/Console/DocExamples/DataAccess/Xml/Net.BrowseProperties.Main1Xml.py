# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to enumerate all properties of an OPC XML-DA item. For each property, it displays its Id and description.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *

# Instantiate the client object.
client = EasyDAClient()

try:
    propertyElements = client.BrowseProperties(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DANodeDescriptor('Dynamic/Analog Types/Int'))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

for propertyElement in propertyElements:
    print('PropertyElements("', propertyElement.PropertyId.NumericalValue, '").Description: ', propertyElement.Description, sep='')

# Example output:
#
#PropertyElements("1").Description: Item Canonical DataType
#PropertyElements("2").Description: Item Value
#PropertyElements("3").Description: Item Quality
#PropertyElements("4").Description: Item Timestamp
#PropertyElements("5").Description: Item Access Rights
#PropertyElements("6").Description: Server Scan Rate
#PropertyElements("7").Description: Item EU Type
#PropertyElements("8").Description: Item EU Info
#PropertyElements("102").Description: High EU
#PropertyElements("103").Description: Low EU

##endregion Example
