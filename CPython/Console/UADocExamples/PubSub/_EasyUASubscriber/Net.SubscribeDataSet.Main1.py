# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to subscribe to all dataset messages on an OPC-UA PubSub connection with UDP UADP mapping.
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
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.udp://239.0.0.1')
# In some cases you may have to set the interface (network adapter) name that needs to be used, similarly to
# the statement below. Your actual interface name may differ, of course.
#pubSubConnectionDescriptor.ResourceAddress.InterfaceName = 'Ethernet'

# Instantiate the subscriber object and hook events.
subscriber = EasyUASubscriber()
subscriber.DataSetMessage += dataSetMessage

print('Subscribing...')
IEasyUASubscriberExtension.SubscribeDataSet(subscriber, pubSubConnectionDescriptor)

print('Processing dataset message events for 20 seconds...')
time.sleep(20)

print('Unsubscribing...')
subscriber.UnsubscribeAllDataSets()

print('Waiting for 1 second...')
# Unsubscribe operation is asynchronous, messages may still come for a short while.
time.sleep(1)

subscriber.DataSetMessage -= dataSetMessage

print('Finished.')



# Example output:
#
#Subscribing...
#Processing dataset message events for 20 seconds...
#
##Dataset data: Good; Data; publisher="32", writer=1, class=eae79794-1af7-4f96-8401-4096cd1d8908, fields: 4
#[#0, True {System.Boolean} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#1, 7945 {System.Int32} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#2, 5246 {System.Int32} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#3, 9/30/2019 11:19:14 AM {System.DateTime} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#
#Dataset data: Good; Data; publisher="32", writer=3, class=96976b7b-0db7-46c3-a715-0979884b55ae, fields: 100
#[#0, 45 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#1, 145 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#2, 245 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#3, 345 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#4, 445 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#5, 545 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#6, 645 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#7, 745 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#8, 845 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#9, 945 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#[#10, 1045 {System.Int64} @0001-01-01T00:00:00.000 @@0001-01-01T00:00:00.000; Good]
#...

##endregion Example
