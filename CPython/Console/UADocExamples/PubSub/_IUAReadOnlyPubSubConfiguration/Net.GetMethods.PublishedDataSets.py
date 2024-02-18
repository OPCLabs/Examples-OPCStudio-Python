# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example obtains and prints out information about all published datasets in the OPC UA PubSub configuration.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.BaseLib import *
#from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *
from OpcLabs.EasyOpc.UA.PubSub.Configuration.Extensions import *
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

    # Get the names of all published datasets in the PubSub configuration.
    publishedDataSetNames = IUAReadOnlyPubSubConfigurationExtension.ListAllPublishedDataSetNames(pubSubConfiguration)

    for publishedDataSetName in publishedDataSetNames:
        print('Published dataset: ', publishedDataSetName, sep='')

        # You can use the statement below to obtain parameters of the published dataset.
        #publishedDataSetElement = IUAReadOnlyPubSubConfigurationExtension.GetPublishedDataSetElement(
        #    pubSubConfiguration,
        #    publishedDataSetName)

except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Finished.')

##endregion Example
