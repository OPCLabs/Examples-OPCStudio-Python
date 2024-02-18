# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
#  This example shows how to acknowledge an OPC UA event.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from System.Collections.Generic import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.Navigation import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')

# Define which alarm we will work with.
alarmNodeDescriptor = UANodeDescriptor(UANodeId(
    'http://opcfoundation.org/Quickstarts/AlarmCondition',  # namespaceUriString
    '1:Colours/EastTank?Yellow'))   # identifier

# Knowing the alarm node, and the fact that is an instance of NonExclusiveLevelAlarmType (or its subtype),
# determine what is its LowState/Id node.
lowStateIdBrowsePathElements = List[UABrowsePathElement]()
lowStateIdBrowsePathElements.Add(UABrowsePathElement.CreateSimple(UAQualifiedName('ns=0;s=LowState')))
lowStateIdBrowsePathElements.Add(UABrowsePathElement.CreateSimple(UAQualifiedName('ns=0;s=Id')))
lowStateIdNodeDescriptor = UANodeDescriptor(UABrowsePath(alarmNodeDescriptor, lowStateIdBrowsePathElements))

# Instantiate the client objects
client = EasyUAClient()

print('Reading the alarm state...')
try:
    lowStateId = IEasyUAClientExtension.ReadValue(client, endpointDescriptor, lowStateIdNodeDescriptor)
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Id of LowState: ', lowStateId, sep='')

print()
print('Finished.')

##endregion Example
