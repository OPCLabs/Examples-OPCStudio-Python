# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to set parameters specific to JSON message mapping.
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
from OpcLabs.EasyOpc.UA.PubSub.Configuration import *
from OpcLabs.EasyOpc.UA.PubSub.Engine import *
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
# Specify the transport protocol mapping.
# The statement below isn't actually necessary, due to automatic message mapping recognition feature; see
# https://kb.opclabs.com/OPC_UA_PubSub_Automatic_Message_Mapping_Recognition for more details.
pubSubConnectionDescriptor.TransportProfileUriString = UAPubSubTransportProfileUriStrings.MqttJson

# Set a custom property on the PubSub connection that influences how the JSON parsing works.
# We are instructing the message parser to turn off the automatic recognition of message format.
# For more details, see https://kb.opclabs.com/OPC_UA_PubSub_JSON_mapping_component .
pubSubConnectionDescriptor.CustomPropertyValueDictionary.set_Item(
    UAQualifiedName(
        '{OpcLabs}',
        'OpcLabs.EasyOpc.UA.Toolkit.PubSub.Sdk.JsonReceiveMessageMapping.MessageParsingParameters.AutoRecognizeMessageFormat'), False)

# Define the arguments for subscribing to the dataset.
subscribeDataSetArguments = UASubscribeDataSetArguments(pubSubConnectionDescriptor)
subscribeDataSetArguments.DataSetSubscriptionDescriptor.CommunicationParameters.BrokerDataSetReaderTransportParameters.\
    QueueName = 'opcuademo/json'
# We must set the DataSetFieldContentMask when the format auto-recognition is turned off.
subscribeDataSetArguments.DataSetSubscriptionDescriptor.CommunicationParameters.\
    DataSetFieldContentMask = UADataSetFieldContentMask.RawData
# We must set the DataSetMessageContentMask when the format auto-recognition is turned off.
subscribeDataSetArguments.DataSetSubscriptionDescriptor.CommunicationParameters.JsonDataSetReaderMessageParameters.\
    DataSetMessageContentMask =\
        UAJsonDataSetMessageContentMask.DataSetWriterId |\
        UAJsonDataSetMessageContentMask.SequenceNumber |\
        UAJsonDataSetMessageContentMask.Status
# We must set the NetworkMessageContentMask when the format auto-recognition is turned off.
subscribeDataSetArguments.DataSetSubscriptionDescriptor.CommunicationParameters.JsonDataSetReaderMessageParameters.\
    NetworkMessageContentMask =\
        UAJsonNetworkMessageContentMask.NetworkMessageHeader |\
        UAJsonNetworkMessageContentMask.DataSetMessageHeader |\
        UAJsonNetworkMessageContentMask.PublisherId
subscribeDataSetArguments.DataSetSubscriptionDescriptor.Filter.DataSetWriterDescriptor = UADataSetWriterDescriptor(1)

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
