# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.
##region Example
# This example demonstrates the loggable entries originating in the OPC-UA client engine and the EasyUAClient component.

# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc
import time

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA import *
from OpcLabs.EasyOpc.UA.OperationModel import *


# Event handler for the LogEntry event. It simply prints out the event.
def onLogEntry(sender, logEntryEventArgs):
    print(logEntryEventArgs)


endpointDescriptor = UAEndpointDescriptor('opc.tcp://opcua.demo-this.com:51210/UA/SampleServer')
# or 'http://opcua.demo-this.com:51211/UA/SampleServer' (currently not supported)
# or 'https://opcua.demo-this.com:51212/UA/SampleServer/'

# Hook static events.
EasyUAClient.LogEntry += onLogEntry

# Instantiate the client object.
client = EasyUAClient()

# Do something - invoke an OPC read, to trigger some loggable entries.
try:
    value = IEasyUAClientExtension.ReadValue(client,
                                             endpointDescriptor,
                                             UANodeDescriptor('nsu=http://test.org/UA/Data/ ;i=10853'))
except UAException as uaException:
    print('*** Failure: ' + uaException.GetBaseException().Message)
    exit()

print('Processing log entry events for 1 minute...')
time.sleep(60)

print()
print('Finished.')

##endregion Example
