# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to subscribe to MQTT dataset messages stored in a file system. This can be used e.g. for
# troubleshooting.
#
# A related example (SubscribeDataSet.MqttTcpSaveCopy) shows how to capture the MQTT messages into the file system.
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


# Define the PubSub connection we will work with. By specifying a file (file URI) with the directory path, MQTT
# messages will be provided from the file storage.
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit(r'C:\MqttReceived')

# Define the arguments for subscribing to the dataset, specifying the MQTT topic name.
subscribeDataSetArguments = UASubscribeDataSetArguments(pubSubConnectionDescriptor)
subscribeDataSetArguments.DataSetSubscriptionDescriptor.CommunicationParameters.BrokerDataSetReaderTransportParameters.\
    QueueName = 'opcuademo/json/#'

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
