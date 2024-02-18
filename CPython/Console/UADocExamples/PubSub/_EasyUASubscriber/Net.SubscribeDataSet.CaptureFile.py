# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to feed the packet capture file into the PubSub subscriber, instead of connecting to the
# message oriented middleware (receiving the messages from the network).
#
# The OpcLabs.Pcap assembly needs to be referenced in your project (or otherwise made available, together with its
# dependencies) for the capture files to work. Refer to the documentation for more information.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import opclabs_pcap
import time

# Import .NET namespaces.
from System import *
from OpcLabs.EasyOpc.UA.PubSub import *
from OpcLabs.EasyOpc.UA.PubSub.Extensions import *
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
# "opc.eth" is the scheme for OPC UA Ethernet. "FF-FF-FF-FF-FF-FF" is the Ethernet broadcast address.
pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.eth://FF-FF-FF-FF-FF-FF')
# Use packets from the specified Ethernet capture file. The file itself is at the root of the project, and we
# have specified that it has to be copied to the project's output directory.
# Note that .pcap is the default file name extension, and can thus be omitted.
UAPubSubConnectionDescriptorExtension.UseEthernetCaptureFile(pubSubConnectionDescriptor,
                                                             'UADemoPublisher-Ethernet.pcap')

# Alternative setup for Ethernet with VLAN tagging:
#pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.eth://FF-FF-FF-FF-FF-FF:2')
#UAPubSubConnectionDescriptorExtension.UseEthernetCaptureFile(pubSubConnectionDescriptor,
#                                                             'UADemoPublisher-EthernetVlan.pcap')

# Alternative setup for UDP over IPv4:
#pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.udp://239.0.0.1')
#UAPubSubConnectionDescriptorExtension.UseEthernetCaptureFile(pubSubConnectionDescriptor,
#                                                             'UADemoPublisher-UDP.pcap')

# Alternative setup for UDP over IPv6:
#pubSubConnectionDescriptor = UAPubSubConnectionDescriptor.op_Implicit('opc.udp://[ff02::1]')
#UAPubSubConnectionDescriptorExtension.UseEthernetCaptureFile(pubSubConnectionDescriptor,
#                                                             'UADemoPublisher-UDP6.pcap')

# Instantiate the subscriber object.
subscriber = EasyUASubscriber()

# Define the arguments for subscribing to the dataset, where the filter is (unsigned 64-bit) publisher Id 31.
subscribeDataSetArguments = UASubscribeDataSetArguments(
    pubSubConnectionDescriptor,
    UASubscribeDataSetFilter(UAPublisherId.CreateUInt64(Decimal(31))))

print('Subscribing...')
IEasyUASubscriberExtension.SubscribeDataSet(subscriber,
                                            subscribeDataSetArguments,
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
