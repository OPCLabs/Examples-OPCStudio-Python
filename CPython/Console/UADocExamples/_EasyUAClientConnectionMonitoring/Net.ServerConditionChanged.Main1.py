# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to monitor connections to and disconnections from the OPC UA server.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from Microsoft.Extensions.DependencyInjection import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *
from OpcLabs.EasyOpc.UA.Services import *


def dataChangeNotification(sender, e):
    # Display value.
    if e.Succeeded:
        print('Value: ', e.AttributeData.Value, sep='')
    else:
        print('*** Failure: ', e.ErrorMessageBrief, sep='')

def onServerConditionChanged(sender, e):
    # Display the event.
    print(e)


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = None
try:
    client = EasyUAClient()

    # Obtain the client connection monitoring service.
    clientConnectionMonitoring = ServiceProviderServiceExtensions.GetService[IEasyUAClientConnectionMonitoring](client)
    if clientConnectionMonitoring is None:
        print('The client connection monitoring service is not available.')
        exit()

    # Hook events
    client.DataChangeNotification += dataChangeNotification
    clientConnectionMonitoring.ServerConditionChanged += onServerConditionChanged

    try:
        print('Reading (1)')
        # The first read will cause a connection to the server.
        attributeData1 = IEasyUAClientExtension.Read(client,
                                                     endpointDescriptor,
                                                     UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
        print(attributeData1)

        print('Reading (2)')
        # The second read, because it closely follows the first one, will reuse the connection that is already
        # open.
        attributeData2 = IEasyUAClientExtension.Read(client,
                                                     endpointDescriptor,
                                                     UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
        print(attributeData2)

    except UAException as uaException:
        print('*** Failure: ' + uaException.GetBaseException().Message)

    print('Waiting for 10 seconds...')
    # Since the connection is now not used for some time, it will be closed.
    time.sleep(10)

    print('Subscribing...')
    # Subscribing to a monitored item will cause a connection to the server, if one is not yet open.
    IEasyUAClientExtension.SubscribeDataChange(client,
                                               endpointDescriptor,
                                               UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'),
                                               1000)

    print('Waiting for 10 seconds...')
    # The connection will not be closed as long as there are any subscriptions to the server.
    time.sleep(10)

    print('Unsubscribing...')
    client.UnsubscribeAllMonitoredItems()

    print('Waiting for 10 seconds...')
    # After some delay, the connection will be closed, because there are no subscriptions to the server.
    time.sleep(10)

    print('Finished.')

finally:
    client and client.Dispose()

##endregion Example
