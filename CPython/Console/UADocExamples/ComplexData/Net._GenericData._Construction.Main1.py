# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows different ways of constructing generic data.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from System.Collections import *
from OpcLabs.BaseLib.DataTypeModel import *


# Create enumeration data with value of 1.
enumerationData = EnumerationData(1)
print(enumerationData)

# Create opaque data from an array of 2 bytes, specifying its size as 15 bits.
opaqueData1 = OpaqueData(
    [0xAA, 0x55],
    15) # sizeInBits
print(opaqueData1)

# Create opaque data from a bit array.
bitArray = BitArray(5)
bitArray[0] = False
bitArray[1] = True
bitArray[2] = False
bitArray[3] = True
bitArray[4] = False
opaqueData2 = OpaqueData(bitArray)
print(opaqueData2)

# Create primitive data with System.Double value of 180.0.
primitiveData1 = PrimitiveData(180.0)
print(primitiveData1)

# Create primitive data with System.String value.
primitiveData2 = PrimitiveData('Temperature is too high!')
print(primitiveData2)

# Create sequence data with two elements, using the Add method.
sequenceData2 = SequenceData()
sequenceData2.Elements.Add(opaqueData1)
sequenceData2.Elements.Add(opaqueData2)
print(sequenceData2)

# Create structured data with two members, using the Add method.
structuredData2 = StructuredData()
structuredData2.Add('Message', primitiveData2)
structuredData2.Add('Status', enumerationData)
print(structuredData2)

# Create union data.
unionData1 = UnionData('DoubleField', primitiveData1)
print(unionData1)

print()
print('Finished.')

##endregion Example
