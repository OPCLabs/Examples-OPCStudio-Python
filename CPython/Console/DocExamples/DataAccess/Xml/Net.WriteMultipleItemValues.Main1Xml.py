# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example

# Shows how to write into multiple OPC XML-DA items using a single method call, and read multiple item values back.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


# Instantiate the client object.
client = EasyDAClient()

print('Writing multiple item values...')
resultArray = client.WriteMultipleItemValues(
    [
        DAItemValueArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Static/Analog Types/Int'), Int32(12345)),
        DAItemValueArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Static/Simple Types/Boolean'), True),
        DAItemValueArguments(ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DAItemDescriptor('Static/Analog Types/Double'), 234.56)
    ])

for i, result in enumerate(resultArray):
    assert result is not None
    if result.Succeeded:
        print('resultArray[', i, ']: success', sep='')
    else:
        assert result.Exception is not None
        print('resultArray[', i, '] *** Failure: ', result.ErrorMessageBrief, sep='')

print()
print('Reading multiple item values...')
valueResultArray = IEasyDAClientExtension.ReadMultipleItemValues(client,
    ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'),
    [
        DAItemDescriptor('Static/Analog Types/Int'),
        DAItemDescriptor('Static/Simple Types/Boolean'),
        DAItemDescriptor('Static/Analog Types/Double')
    ])

for i, valueResult in enumerate(valueResultArray):
    assert valueResult is not None
    if valueResult.Succeeded:
        print('valueResultArray[', i, '].Value: ', valueResult.Value, sep='')
    else:
        assert valueResult.Exception is not None
        print('valueResultArray[', i, '] *** Failure: ', valueResult.ErrorMessageBrief, sep='')

# Example output:
#
#Writing multiple item values...
#resultArray[0]: success
#resultArray[1]: success
#resultArray[2]: success
#
#Reading multiple item values...
#valueResultArray[0]: Success; 12345 {System.Int32}
#valueResultArray[1]: Success; True {System.Boolean}
#valueResultArray[2]: Success; 234.56 {System.Single}

##endregion Example
