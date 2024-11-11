# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to get a value of a single OPC XML-DA property.
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

# Instantiate the client object.
client = EasyDAClient()

# Perform the operation
try:
    value = IEasyDAClientExtension.GetPropertyValue(client, ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DANodeDescriptor('Dynamic/Analog Types/Int'), 
                                                    DAPropertyDescriptor(DAPropertyId(DAPropertyDescriptor.Timestamp)))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

# Display results
print('value: ', value, sep='')

##endregion Example
