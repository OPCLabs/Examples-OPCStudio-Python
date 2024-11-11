# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# This example shows how to lock and unlock connections to an OPC UA server. The component attempts to keep the locked
# connections open, until unlocked.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# Missing some example? Ask us for it on our Online Forums, https://www.opclabs.com/forum/index ! You do not have to own
# a commercial license in order to use Online Forums, and we reply to every post.
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import time
import opclabs_quickopc

# Import .NET namespaces.
from Microsoft.Extensions.DependencyInjection import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *
from OpcLabs.EasyOpc.UA.Services import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object and hook events.
client = None
try:
    client = EasyUAClient()

    # Obtain the client connection monitoring service.
    clientConnectionMonitoring = ServiceProviderServiceExtensions.GetService[IEasyUAClientConnectionMonitoring](client)
    if clientConnectionMonitoring is None:
        print('The client connection monitoring service is not available.')
        exit()

    # Obtain the client connection control service.
    clientConnectionControl = ServiceProviderServiceExtensions.GetService[IEasyUAClientConnectionControl](client)
    if clientConnectionControl is None:
        print('The client connection control service is not available.')
        exit()

    # Display the server condition changed events.
    clientConnectionMonitoring.ServerConditionChanged += lambda sender, args: print(args)

    lockHandle = 0
    locked = False
    try:
        print('Reading (1)')
        # The first read will cause a connection to the server.
        attributeData1 = IEasyUAClientExtension.Read(client,
                                                     endpointDescriptor,
                                                     UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
        print(attributeData1)

        print('Waiting for 10 seconds...')
        # Since the connection is now not used for some time, and it is not locked, it will be closed.
        time.sleep(10)

        print('Locking')
        # Locking the connection causes it to open, if possible.
        lockHandle = clientConnectionControl.LockConnection(endpointDescriptor)
        locked = True

        print('Waiting for 10 seconds...')
        # The connection is locked, it will not be closed now.
        time.sleep(10)

        print('Reading (2)')
        attributeData2 = IEasyUAClientExtension.Read(client,
                                                     endpointDescriptor,
                                                     UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
        print(attributeData2)

        print('Waiting for 10 seconds...')
        # The connection is still locked, it will not be closed now.
        time.sleep(10)

    except UAException as uaException:
        print('*** Failure: ' + uaException.GetBaseException().Message)

    finally:
        if locked:
            print('Unlocking')
            clientConnectionControl.UnlockConnection(lockHandle)

    print('Waiting for 10 seconds...')
    # After some delay, the connection will be closed, because there are no subscriptions to the server and no
    # connection locks.
    time.sleep(10)

    print('Finished.')

finally:
    client and client.Dispose()

##endregion Example
