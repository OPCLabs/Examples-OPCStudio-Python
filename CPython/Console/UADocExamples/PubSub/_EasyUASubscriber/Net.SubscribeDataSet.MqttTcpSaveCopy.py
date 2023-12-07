# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to all dataset messages on an OPC-UA PubSub connection with MQTT (JSON or UADP
# mapping) using TCP, and store a copy of all received messages into a file system.
#
# A related example (SubscribeDataSet.MqttFromFileStorage) shows hot the captured messages can be replayed from the file
# system, e.g. for troubleshooting.
#
# The following package needs to be referenced in your project (or otherwise made available) for the MQTT transport to
# work.
# - OpcLabs.MqttNet
# Refer to the documentation for more information.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import opclabs_mqttnet
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.PubSub import *
from OpcLabs.EasyOpc.UA.PubSub.OperationModel import *


def dataSetMessage(sender, e):
    # Display the dataset.
    if e.Succeeded:
        # An event with null DataSetData just indicates a successful connection.
        if e.DataSetData is not None:
            print('')
            print('Dataset data: ', e.DataSetData, sep='')
            for pair in e.DataSetData.FieldDataDictionary:
                print(pair)
    else:
        print('')
        print('*** Failure: ', e.ErrorMessageBrief, sep='')


# Define the PubSub connection we will work with. Uses implicit conversion from a string.
# Default port with MQTT is 1883.
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('mqtt://opcua-pubsub.demo-this.com')
# Configure the PubSub connection so that a copy of the received messages is stored into the file system, under
# the specified "root" directory.
pubSubConnectionDescriptor.CustomPropertyValueDictionary.set_Item(
    UAQualifiedName('{OpcLabs}', 'MqttFileCopyReceivedRoot'), r'C:\MqttReceived')

# Define the arguments for subscribing to the dataset, specifying the MQTT topic name.
subscribeDataSetArguments = UASubscribeDataSetArguments(pubSubConnectionDescriptor)
subscribeDataSetArguments.DataSetSubscriptionDescriptor.CommunicationParameters.BrokerDataSetReaderTransportParameters.\
    QueueName = 'opcuademo/#'

# Instantiate the subscriber object and hook events.
subscriber = EasyUASubscriber()
subscriber.DataSetMessage += dataSetMessage

print('Subscribing...')
IEasyUASubscriberExtension.SubscribeDataSet(subscriber, subscribeDataSetArguments)

print('Processing dataset message events for 20 seconds...')
time.sleep(20)

print('Unsubscribing...')
subscriber.UnsubscribeAllDataSets()

print('Waiting for 1 second...')
# Unsubscribe operation is asynchronous, messages may still come for a short while.
time.sleep(1)

subscriber.DataSetMessage -= dataSetMessage

print('Finished.')

##endregion Example
