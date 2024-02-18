# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to changes of multiple monitored items and display the value of the monitored item
# with each change.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


def dataChangeNotification(sender, e):
    # Display value.
    if e.Succeeded:
        print(e.Arguments.NodeDescriptor, ': ', e.AttributeData.Value, sep='')
    else:
        print(e.Arguments.NodeDescriptor, ' *** Failure: ', e.ErrorMessageBrief, sep='')


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object and hook events.
client = EasyUAClient()
client.DataChangeNotification += dataChangeNotification

print('Subscribing...')
client.SubscribeMultipleMonitoredItems([
    EasyUAMonitoredItemArguments(
        None,
        endpointDescriptor,
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10845'),
        UAMonitoringParameters(1000)),
    EasyUAMonitoredItemArguments(
        None,
        endpointDescriptor,
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
        UAMonitoringParameters(1000)),
    EasyUAMonitoredItemArguments(
        None,
        endpointDescriptor,
        UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10855'),
        UAMonitoringParameters(1000)),
    ])

print('Processing data change events for 10 seconds...')
time.sleep(10)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
