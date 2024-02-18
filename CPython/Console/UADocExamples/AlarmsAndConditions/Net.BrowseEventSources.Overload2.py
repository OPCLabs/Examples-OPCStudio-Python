# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to browse objects under the "Objects" node and display event sources.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.AddressSpace import *
from OpcLabs.EasyOpc.UA.AddressSpace.Standard import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which server we will work with.
endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')


def browseFrom(nodeDescriptor):
    global endpointDescriptor

    print()
    print()
    print('Parent node: ', nodeDescriptor, sep='')

    # Instantiate the client object.
    client = EasyUAClient()

    # Obtain event sources.
    eventSourceNodeElementCollection = IEasyUAClientExtension.BrowseEventSources(client,
                                                                                 endpointDescriptor,
                                                                                 nodeDescriptor)

    # Display event sources.
    if eventSourceNodeElementCollection.Count != 0:
        print('')
        print('Event sources:')
        for eventSourceNodeElement in eventSourceNodeElementCollection:
            print(eventSourceNodeElement)

    # Obtain objects.
    objectNodeElementCollection = IEasyUAClientExtension.BrowseObjects(client,
                                                                       endpointDescriptor,
                                                                       nodeDescriptor)

    # Recurse.
    for objectNodeElement in objectNodeElementCollection:
        browseFrom(objectNodeElement.ToUANodeDescriptor())


# Start browsing from the "Objects" node.
try:
    browseFrom(UANodeDescriptor(UAObjectIds.ObjectsFolder))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print()
print('Finished.')

##endregion Example
