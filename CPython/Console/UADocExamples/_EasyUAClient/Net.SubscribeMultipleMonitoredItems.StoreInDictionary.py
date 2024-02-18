# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to store current state of the subscribed monitored items in a dictionary.
# each change.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import threading
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


lock = threading.Lock()
attributeDataResultDictionary = {}

# Data change notification event handler.
def dataChangeNotification(sender, eventArgs):
    global lock
    global attributeDataResultDictionary
    with lock:
        # Convert the event arguments to a UAAttributeData result object, and store it in the dictionary under the
        # key which is the node descriptor of the monitored item this data change notification is for.
        attributeDataResultDictionary[eventArgs.Arguments.NodeDescriptor] = EasyUADataChangeNotificationEventArgs.ToUAAttributeDataResult(eventArgs)


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = EasyUAClient()
# Hook events.
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

print('Processing data change events for 1 minute...')
endTime = time.time() + 60
while time.time() < endTime:
    time.sleep(5)
    #
    # Each 5 seconds, display the current state of the monitored items we have subscribed to.
    with lock:
        print()
        print('Current state of the monitored items:')
        for nodeDescriptor, attributeDataResult in attributeDataResultDictionary.items():
            print(nodeDescriptor, ': ', attributeDataResult, sep='')
        #
        # The code above shows how you can process the complete contents of the dictionary. In other
        # scenarios, you may want to access just a specific entry in the dictionary. You can achieve that
        # by indexing the dictionary by the node descriptor of the monitored item you are interested in.

print()
print('Unsubscribing all monitored items...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
