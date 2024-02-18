# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to changes of a monitored item with data change filter.
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
        print('Value: ', e.AttributeData.Value, sep='')
    else:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object and hook events.
client = EasyUAClient()
client.DataChangeNotification += dataChangeNotification

print('Subscribing...')
# Report a notification if either the StatusCode or the value change.
# The UADataChangeTrigger has an implicit conversion to UADataChangeFilter.
IEasyUAClientExtension.SubscribeDataChange(client,
    endpointDescriptor,
    UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
    1000,
    UADataChangeFilter(UADataChangeTrigger.StatusValue))

print('Processing data change events for 20 seconds...')
time.sleep(20)

print('Unsubscribing...')
client.UnsubscribeAllMonitoredItems()

print('Waiting for 5 seconds...')
time.sleep(5)

print('Finished.')

##endregion Example
