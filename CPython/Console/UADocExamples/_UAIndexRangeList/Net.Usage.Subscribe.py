# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to range of values from an array.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def dataChangeNotification(sender, eventArgs):
    # Display value.
    if eventArgs.Succeeded:
        arrayValue = eventArgs.AttributeData.Value
        print('Value: {', ", ".join(["{}"]*len(arrayValue)).format(*arrayValue), '}', sep='')
    else:
        print('*** Failure: ', eventArgs.ErrorMessageBrief, sep='')


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()

print('Subscribing to range...')
attributeArguments = UAAttributeArguments(endpointDescriptor, UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10933'))
attributeArguments.IndexRangeList = UAIndexRangeList.OneDimension(2, 4)
monitoredItemArguments = UAMonitoredItemArguments(attributeArguments, UAMonitoringParameters(1000))
IEasyUAClientExtension.SubscribeMonitoredItem(client,
    monitoredItemArguments,
    EasyUADataChangeNotificationEventHandler(dataChangeNotification))

print('Processing data change events for 10 seconds...')
time.sleep(10)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 2 seconds...')
time.sleep(2)

print('Finished.')

##endregion Example
