# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to dataset messages, specifying just the published dataset name, and resolving all
# the dataset subscription arguments from an OPC-UA PubSub configuration file.
#
# In order to produce network messages for this example, run the UADemoPublisher tool. For documentation, see
# https://kb.opclabs.com/UADemoPublisher_Basics . In some cases, you may have to specify the interface name to be used.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.BaseLib import *
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


# Define the PubSub resolver. We want the information be resolved from a PubSub binary configuration file that
# we have. The file itself is in this script's directory.
pubSubResolverDescriptor = UAPubSubResolverDescriptor.File(ResourceDescriptor('UADemoPublisher-Default.uabinary'))

# Instantiate the subscriber object.
subscriber = EasyUASubscriber()

print('Subscribing...')
# Specify the published dataset name, and let all other subscription arguments be resolved automatically.
IEasyUASubscriberExtension.SubscribeDataSet(subscriber,
                                            pubSubResolverDescriptor,
                                            'AllTypes-Dynamic',
                                            EasyUADataSetMessageEventHandler(dataSetMessage))

print('Processing dataset message events for 20 seconds...')
time.sleep(20)

print('Unsubscribing...')
subscriber.UnsubscribeAllDataSets()

print('Waiting for 1 second...')
# Unsubscribe operation is asynchronous, messages may still come for a short while.
time.sleep(1)

print('Finished.')

##endregion Example
