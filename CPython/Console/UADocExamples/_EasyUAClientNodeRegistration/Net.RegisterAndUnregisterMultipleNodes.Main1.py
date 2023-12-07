# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example shows how to register and unregister multiple nodes in an OPC UA server, and use this approach together
# with connection locking.
#
# Node registration (with OPC UA servers that support it) can improve performance with repeatedly accessed nodes.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from Microsoft.Extensions.DependencyInjection import *
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *
from OpcLabs.EasyOpc.UA.Services import *
from OpcLabs.EasyOpc.UA.Services.Extensions import *


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Instantiate the client object.
client = None
try:
    client = EasyUAClient()

    # Obtain the client connection monitoring service.
    clientNodeRegistration = ServiceProviderServiceExtensions.GetRequiredService[IEasyUAClientNodeRegistration](client)
    if clientNodeRegistration is None:
        print('The client connection monitoring service is not available.')
        exit()

    # Obtain the client connection control service.
    clientConnectionControl = ServiceProviderServiceExtensions.GetRequiredService[IEasyUAClientConnectionControl](client)
    if clientConnectionControl is None:
        print('The client connection control service is not available.')
        exit()

    nodeDescriptorArray = [
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[0]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[4]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[8]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[12]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[16]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[20]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[24]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[28]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[32]'),
        UANodeDescriptor('nsu=http://samples.org/UA/memorybuffer/Instance ;ns=8;s=UInt32[36]'),
    ]

    print('Registering nodes')
    registrationHandleArray = IEasyUAClientNodeRegistrationExtension.RegisterMultipleNodes(clientNodeRegistration,
                                                                                           endpointDescriptor,
                                                                                           nodeDescriptorArray)

    print('Locking the connection')
    # Locking the connection will attempt to open it, and when successful, the nodes will be registered with
    # the server at that time. The use of locking is not necessary, but it may bring benefits together with the
    # node registration. See the conceptual documentation for more information.
    lockHandle = clientConnectionControl.LockConnection(endpointDescriptor)

    print('Waiting for 10 seconds...')
    # The example uses this delay to demonstrate the fact that your code might have other tasks to do, before
    # it accesses the previously registered nodes.
    time.sleep(10)

    print('Reading (1)')
    attributeDataResultArray1 = IEasyUAClientExtension.ReadMultiple(client, endpointDescriptor, nodeDescriptorArray)
    for attributeDataResult in attributeDataResultArray1:
        print(attributeDataResult)

    print('Reading (2)')
    attributeDataResultArray2 = IEasyUAClientExtension.ReadMultiple(client, endpointDescriptor, nodeDescriptorArray)
    for attributeDataResult in attributeDataResultArray2:
        print(attributeDataResult)

    print('Unlocking the connection')
    clientConnectionControl.UnlockConnection(lockHandle)

    print('Unregistering nodes')
    clientNodeRegistration.UnregisterMultipleNodes(registrationHandleArray)

    print('Finished.')

finally:
    client and client.Dispose()

##endregion Example
