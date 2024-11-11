# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows that either a single client object, or multiple client objects can be used to read values from two
# servers.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Define which servers we will work with.
endpointDescriptor1 = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'
endpointDescriptor2 = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:62544/Quickstarts/AlarmConditionServer')


# Part 1: Use a single client object.
# This demonstrates the fact that the client objects do *not* represent connections to individual servers.
# Instead, they are able to maintain connections to multiple servers internally. API method calls on the client
# object include the server's endpoint descriptor in their arguments, so you can specify a different endpoint
# with each operation.
print()

# Instantiate the client object.
client = EasyUAClient()

print('Obtaining values of nodes using a single client object...')
try:
    # The node Id we are reading returns the product name of the server.
    value1 = IEasyUAClientExtension.ReadValue(client,
                                              endpointDescriptor1,
                                              UANodeDescriptor('nsu=http://opcfoundation.org/UA/ ;i=2261'))
    value2 = IEasyUAClientExtension.ReadValue(client,
                                              endpointDescriptor2,
                                              UANodeDescriptor('nsu=http://opcfoundation.org/UA/ ;i=2261'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('value1: ', value1, sep='')
print('value2: ', value2, sep='')


# Part 2: Use multiple client objects.
# This demonstrates the fact that it is also possible to use multiple client objects, and on the OPC side, the
# behavior will be the same as if you had used a single client object. Multiple client objects consume somewhat
# more resources on the client side, but they come handy if, for example,
# - you cannot easily pass around the single pre-created client object to various parts in your code, or
# - you are using subscriptions, and you want to hook separate event handlers for different purposes, or
# - you need to set something in the instance parameters of the client object differently for different
# connections.
print()

# Instantiate the client objects.
client1 = EasyUAClient()
client2 = EasyUAClient()

print('Obtaining values of nodes using multiple client objects...')
try:
    # The node Id we are reading returns the product name of the server.
    value1 = IEasyUAClientExtension.ReadValue(client1,
                                              endpointDescriptor1,
                                              UANodeDescriptor('nsu=http://opcfoundation.org/UA/ ;i=2261'))
    value2 = IEasyUAClientExtension.ReadValue(client2,
                                              endpointDescriptor2,
                                              UANodeDescriptor('nsu=http://opcfoundation.org/UA/ ;i=2261'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

# Display results.
print('value1: ', value1, sep='')
print('value2: ', value2, sep='')


print()
print('Finished.')

##endregion Example
