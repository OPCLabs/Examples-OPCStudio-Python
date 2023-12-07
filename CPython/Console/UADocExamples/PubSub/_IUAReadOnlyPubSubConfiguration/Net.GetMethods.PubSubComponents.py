# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example obtains and prints out information about PubSub connections, writer groups, and dataset writers in the
# OPC UA PubSub configuration.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib import *
#from OpcLabs.EasyOpc.UA import *
#from OpcLabs.EasyOpc.UA.PubSub.Configuration.Extensions import *
from OpcLabs.EasyOpc.UA.OperationModel import *
from OpcLabs.EasyOpc.UA.PubSub.InformationModel import *
from OpcLabs.EasyOpc.UA.PubSub.InformationModel.Extensions import *
from OpcLabs.EasyOpc.UA.PubSub.OperationModel import *


# Instantiate the publish-subscribe client object.
publishSubscribeClient = EasyUAPublishSubscribeClient()

try:
    print('Loading the configuration...')
    # Load the PubSub configuration from a file. The file itself is in this script's directory.
    pubSubConfiguration = IEasyUAPublishSubscribeClientExtension.LoadReadOnlyConfiguration(publishSubscribeClient,
        'UADemoPublisher-Default.uabinary')

    # Alternatively, using the statement below, you can access a live configuration residing in an OPC UA
    # Server with appropriate information model.
    #pubSubConfiguration = publishSubscribeClient.AccessReadOnlyConfiguration(
    #    UAEndpointDescriptor('opc.tcp://localhost:48010'))

    # Get the names of PubSub connections in the configuration, regardless of the folder they reside in.
    pubSubConnectionNames = pubSubConfiguration.ListConnectionNames()
    for pubSubConnectionName in pubSubConnectionNames:
        print('PubSub connection: ', pubSubConnectionName, sep='')

        # You can use the statement below to obtain parameters of the PubSub connection.
        #connectionElement = IUAReadOnlyPubSubConfigurationExtension.GetConnectionElement(pubSubConfiguration,
        #    pubSubConnectionName)

        # Get names of the writer groups on this PubSub connection.
        writerGroupNames = pubSubConfiguration.ListWriterGroupNames(pubSubConnectionName)
        for writerGroupName in writerGroupNames:
            print('  Writer group: ', writerGroupName, sep='')

            # You can use the statement below to obtain parameters of the writer group.
            #writerGroupElement = IUAReadOnlyPubSubConfigurationExtension.GetWriterGroupElement(pubSubConfiguration,
            #    pubSubConnectionName, writerGroupName)

            # Get names of the dataset writers on this writer group.
            dataSetWriterNames = pubSubConfiguration.ListDataSetWriterNames(pubSubConnectionName, writerGroupName)
            for dataSetWriterName in dataSetWriterNames:
                print('    Dataset writer: ', dataSetWriterName, sep='')

                # You can use the statement below to obtain parameters of the dataset writer.
                #dataSetWriterElement = IUAReadOnlyPubSubConfigurationExtension.GetDataSetWriterElement(pubSubConfiguration,
                #    pubSubConnectionName, writerGroupName, dataSetWriterName)

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
