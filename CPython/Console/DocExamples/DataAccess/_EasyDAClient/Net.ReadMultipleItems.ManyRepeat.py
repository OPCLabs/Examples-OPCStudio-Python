# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example repeatedly reads a large number of items.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.DataAccess.OperationModel import *
from OpcLabs.EasyOpc.OperationModel import *


REPEAT_COUNT = 10
NUMBER_OF_ITEMS = 1000

print('Creating array of arguments...')
argumentArray = [None]*NUMBER_OF_ITEMS
for i in range(NUMBER_OF_ITEMS):
    copy = (i//100) + 1
    phase = i % 100
    itemId = 'Simulation.Incrementing.Copy_{}.Phase_{}'.format(copy, phase)
    print(itemId)
    #
    readItemArguments = DAReadItemArguments(ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor(itemId))
    argumentArray[i] = readItemArguments

# Instantiate the client object.
client = EasyDAClient()

#
for iRepeat in range(1, REPEAT_COUNT + 1):
    print('Reading items...')
    vtqResultArray = client.ReadMultipleItems(argumentArray)
    #
    successCount = 0
    for vtqResult in vtqResultArray:
        if vtqResult.Succeeded:
            successCount = successCount + 1
        print('Success count: ', successCount, sep='')

print('Finished.')

##endregion Example
