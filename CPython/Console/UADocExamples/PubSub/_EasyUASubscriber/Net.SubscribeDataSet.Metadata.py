# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to dataset messages with RawData field encoding, specifying the metadata necessary
# for their decoding directly in the code.
#
# In order to produce network messages for this example, run the UADemoPublisher tool. For documentation, see
# https://kb.opclabs.com/UADemoPublisher_Basics . In some cases, you may have to specify the interface name to be used.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.PubSub import *
from OpcLabs.EasyOpc.UA.PubSub.Configuration import *
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
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.udp://239.0.0.1')
# In some cases you may have to set the interface (network adapter) name that needs to be used, similarly to
# the statement below. Your actual interface name may differ, of course.
#pubSubConnectionDescriptor.ResourceAddress.InterfaceName = 'Ethernet'

# Define the filter. Publisher Id (unsigned 16-bits) is 30, and the writer group Id is 101.
# The dataset writer Id (1) must not be specified in the filter, because it does not appear in the message.
filter = UASubscribeDataSetFilter(UAPublisherId.CreateUInt16(30),
                                  UAWriterGroupDescriptor(101))

# Define the metadata.
metaData = UADataSetMetaData()
metaData.Add(UAFieldMetaData('BoolToggle', UABuiltInType.Boolean))
metaData.Add(UAFieldMetaData('Int32', UABuiltInType.Int32))
metaData.Add(UAFieldMetaData('Int32Fast', UABuiltInType.Int32))
metaData.Add(UAFieldMetaData('DateTime', UABuiltInType.DateTime))

# Define the dataset subscription, with specific communication parameters.
# The dataset offset is needed with messages that do not contain dataset writer Ids and use RawData field
# encoding. An exception to this rule is when the dataset is the only or first in the dataset message payload,
# which is also the case here, but we are specifying the dataset offset anyway, for illustration.
dataSetSubscriptionDescriptor = UADataSetSubscriptionDescriptor(pubSubConnectionDescriptor, filter, metaData)
dataSetSubscriptionDescriptor.CommunicationParameters.UadpDataSetReaderMessageParameters.DataSetOffset = 15

# Instantiate the subscriber object and hook events.
subscriber = EasyUASubscriber()
subscriber.DataSetMessage += dataSetMessage

print('Subscribing...')
subscriber.SubscribeDataSet(EasyUASubscribeDataSetArguments(dataSetSubscriptionDescriptor))

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
