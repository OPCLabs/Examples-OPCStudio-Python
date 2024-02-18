# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows different ways of constructing OPC UA node IDs.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Parsing import *
from OpcLabs.EasyOpc.UA.AddressSpace.Parsing.Extensions import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *


# A node ID specifies a namespace (either by an URI or by an index), and an identifier.
# The identifier can be numeric (an integer), string, GUID, or opaque.
#


# A node ID can be specified in string form (so-called expanded text).
# The code below specifies a namespace URI (nsu=...), and an integer identifier (i=...).
nodeId1 = UANodeId('nsu=http://test.org/UA/Data/ ;i=10853')
print(nodeId1)


# Similarly, with a string identifier (s=...).
nodeId2 = UANodeId('nsu=http://test.org/UA/Data/ ;s=someIdentifier')
print(nodeId2)


# Actually, "s=" can be omitted (not recommended, though).
nodeId3 = UANodeId('nsu=http://test.org/UA/Data/ ;someIdentifier')
print(nodeId3)


# Similarly, with a GUID identifier (g=...).
nodeId4 = UANodeId('nsu=http://test.org/UA/Data/ ;g=BAEAF004-1E43-4A06-9EF0-E52010D5CD10')
print(nodeId4)


# Similarly, with an opaque identifier (b=..., in Base64 encoding).
nodeId5 = UANodeId('nsu=http://test.org/UA/Data/ ;b=AP8=')
print(nodeId5)


# Namespace index can be used instead of namespace URI. The server is allowed to change the namespace
# indices between sessions (except for namespace 0), and for this reason, you should avoid the use of
# namespace indices, and rather use the namespace URIs whenever possible.
nodeId6 = UANodeId('ns=2;i=10853')
print(nodeId6)


# Namespace index can be also specified together with namespace URI. This is still safe, but may be
# a bit quicker to perform, because the client can just verify the namespace URI instead of looking
# it up.
nodeId7 = UANodeId('nsu=http://test.org/UA/Data/ ;ns=2;i=10853')
print(nodeId7)


# When neither namespace URI nor namespace index are given, the node ID is assumed to be in namespace
# with index 0 and URI "http://opcfoundation.org/UA/", which is reserved by OPC UA standard. There are
# many standard nodes that live in this reserved namespace, but no nodes specific to your servers will
# be in the reserved namespace, and hence the need to specify the namespace with server-specific nodes.
nodeId8 = UANodeId('i=2254')
print(nodeId8)


# If you attempt to pass in a string that does not conform to the syntax rules,
# a UANodeIdFormatException is thrown.
try:
    nodeId9 = UANodeId('nsu=http://test.org/UA/Data/ ;i=notAnInteger')
except UANodeIdFormatException as nodeIdFormatException:
    print('*** Failure: ', nodeIdFormatException.Message, sep='')


# There is a parser object that can be used to parse the expanded texts of node IDs.
nodeIdParser10 = UANodeIdParser()
nodeId10 = IUANodeIdParserExtension.Parse(nodeIdParser10, 'nsu=http://test.org/UA/Data/ ;i=10853')
print(nodeId10)


# The parser can be used if you want to parse the expanded text of the node ID but do not want
# exceptions be thrown.
nodeIdParser11 = UANodeIdParser()
stringParsingError, nodeId11 = IUANodeIdParserExtension.TryParse(nodeIdParser11,
                                                                 'nsu=http://test.org/UA/Data/ ;i=notAnInteger',
                                                                 UANodeId())    # placeholder for 'out'
if stringParsingError is None:
    print(nodeId11)
else:
    print('*** Failure: ', stringParsingError.Message, sep='')


# You can also use the parser if you have node IDs where you want the default namespace be different
# from the standard "http://opcfoundation.org/UA/".
nodeIdParser12 = UANodeIdParser('http://test.org/UA/Data/')
nodeId12 = IUANodeIdParserExtension.Parse(nodeIdParser12, 'i=10853')
print(nodeId12)


# The namespace URI string (or the namespace index, or both) and the identifier can be passed to the
# constructor separately.
nodeId13 = UANodeId('http://test.org/UA/Data/', 10853)
print(nodeId13)


# You can create a "null" node ID. Such node ID does not actually identify any valid node in OPC UA, but
# is useful as a placeholder or as a starting point for further modifications of its properties.
nodeId14 = UANodeId()
print(nodeId14)


# Properties of a node ID can be modified individually. The advantage of this approach is that you do
# not have to care about syntax of the node ID expanded text.
nodeId15 = UANodeId()
nodeId15.NamespaceUriString = 'http://test.org/UA/Data/'
nodeId15.Identifier = 10853
print(nodeId15)


# If you know the type of the identifier upfront, it is safer to use typed properties that correspond
# to specific types of identifier. Here, with an integer identifier.
nodeId17 = UANodeId()
nodeId17.NamespaceUriString = 'http://test.org/UA/Data/'
nodeId17.NumericIdentifier = 10853
print(nodeId17)


# Similarly, with a string identifier.
nodeId18 = UANodeId()
nodeId18.NamespaceUriString = 'http://test.org/UA/Data/'
nodeId18.StringIdentifier = 'someIdentifier'
print(nodeId18)


# Similarly, with a GUID identifier.
nodeId19 = UANodeId()
nodeId19.NamespaceUriString = 'http://test.org/UA/Data/'
nodeId19.GuidIdentifier = Guid.Parse('BAEAF004-1E43-4A06-9EF0-E52010D5CD10')
print(nodeId19)


# If you have GUID in its string form, the node ID object can parse it for you.
nodeId20 = UANodeId()
nodeId20.NamespaceUriString = 'http://test.org/UA/Data/'
nodeId20.GuidIdentifierString = 'BAEAF004-1E43-4A06-9EF0-E52010D5CD10'
print(nodeId20)


# And, with an opaque identifier.
nodeId21 = UANodeId()
nodeId21.NamespaceUriString = 'http://test.org/UA/Data/'
nodeId21.OpaqueIdentifier = [0x00, 0xFF]
print(nodeId21)


# Assigning an expanded text to a node ID parses the value being assigned and sets all corresponding
# properties accordingly.
nodeId22 = UANodeId()
nodeId22.ExpandedText = 'nsu=http://test.org/UA/Data/ ;i=10853'
print(nodeId22)


# There is a copy constructor as well, creating a clone of an existing node ID.
nodeId24a = UANodeId('nsu=http://test.org/UA/Data/ ;i=10853')
print(nodeId24a)
nodeId24b = UANodeId(nodeId24a)
print(nodeId24b)


# We have provided static classes with properties that correspond to all standard nodes specified by
# OPC UA. You can simply refer to these node IDs in your code.
# The class names are UADataTypeIds, UAMethodIds, UAObjectIds, UAObjectTypeIds, UAReferenceTypeIds,
# UAVariableIds and UAVariableTypeIds.
nodeId25 = UAObjectIds.TypesFolder
print(nodeId25)
# When the UANodeId equals to one of the standard nodes, it is output in the shortened form - as the standard
# name only.


# You can also refer to any standard node using its name (in a string form).
# Note that assigning a non-existing standard name is not allowed, and throws ArgumentException.
nodeId26 = UANodeId()
nodeId26.StandardName = "TypesFolder"
print(nodeId26)


# When you browse for nodes in the OPC UA server, every returned node element contains a node ID that
# you can use further.
client27 = EasyUAClient()
try:
    nodeElementCollection27 = IEasyUAClientExtension.Browse(client27,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor(UAObjectIds.Server),
        UABrowseParameters(UANodeClass.All, UAReferenceTypeIds.References))
    if nodeElementCollection27.Count != 0:
        nodeId27 = nodeElementCollection27.get_Item(0).NodeId
        print(nodeId27)
except UAException as uaException:
    print('*** Failure: ', uaException.GetBaseException().Message, sep='')


# As above, but using a constructor that takes a node element as an input.
client28 = EasyUAClient()
try:
    nodeElementCollection28 = IEasyUAClientExtension.Browse(client28,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor(UAObjectIds.Server),
        UABrowseParameters(UANodeClass.All, UAReferenceTypeIds.References))
    if nodeElementCollection28.Count != 0:
        nodeId28 = UANodeId(nodeElementCollection28.get_Item(0))
        print(nodeId28)
except UAException as uaException:
    print('*** Failure: ', uaException.GetBaseException().Message, sep='')


# Or, there is an explicit conversion from a node descriptor as well.
client29 = EasyUAClient()
try:
    nodeElementCollection29 = IEasyUAClientExtension.Browse(client29,
        UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer'),
        UANodeDescriptor(UAObjectIds.Server),
        UABrowseParameters(UANodeClass.All, UAReferenceTypeIds.References))
    if nodeElementCollection29.Count != 0:
        # FromUANodeDescriptor can be used instead of op_Explicit, too.
        nodeId29 = UANodeId.op_Explicit(UANodeDescriptor(nodeElementCollection29.get_Item(0)))
        print(nodeId29)
except UAException as uaException:
    print('*** Failure: ', uaException.GetBaseException().Message, sep='')


print()
print('Finished.')

##endregion Example
