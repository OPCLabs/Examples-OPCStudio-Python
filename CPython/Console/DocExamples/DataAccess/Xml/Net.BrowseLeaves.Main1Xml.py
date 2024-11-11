# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to obtain all leaves under the "Simulation" branch of the address space. For each leaf, it displays 
# the ItemID of the node.
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
from OpcLabs.EasyOpc.DataAccess.AddressSpace import *
from OpcLabs.EasyOpc.OperationModel import *

# Instantiate the client object.
client = EasyDAClient()

try:
    leafElements = IEasyDAClientExtension.BrowseLeaves(client, ServerDescriptor('http://opcxml.demo-this.com/XmlDaSampleServer/Service.asmx'), DANodeDescriptor('Static/Analog Types'))
except OpcException as opcException:
    print('*** Failure: ' + opcException.GetBaseException().Message, sep='')
    exit()

for leafElement in leafElements:
    print('LeafElements("', leafElement.Name, '").ItemId: ', leafElement.ItemId, sep='')

# Example output:
#
#LeafElements("Int").ItemId: Static/Analog Types/Int
#LeafElements("Double").ItemId: Static/Analog Types/Double
#LeafElements("Int[]").ItemId: Static/Analog Types/Int[]
#LeafElements("Double[]").ItemId: Static/Analog Types/Double[]

##endregion Example
