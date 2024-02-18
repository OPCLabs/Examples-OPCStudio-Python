# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how different data types can be read, including rare types and arrays of values.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc import *
from OpcLabs.EasyOpc.DataAccess import *
from OpcLabs.EasyOpc.OperationModel import *


def readAndDisplay(itemId):
    global client
    #
    print()
    print('Reading "', itemId, '"...', sep='')
    #
    try:
        vtq = IEasyDAClientExtension.ReadItem(client, ServerDescriptor('OPCLabs.KitServer.2'), DAItemDescriptor(itemId))
    except OpcException as opcException:
        print('*** Failure: ' + opcException.GetBaseException().Message)
        return
    print('Vtq: ', vtq, sep='')


# Instantiate the client object.
client = EasyDAClient()

#
readAndDisplay('Simulation.Register_EMPTY')
readAndDisplay('Simulation.Register_NULL')
readAndDisplay('Simulation.Register_DISPATCH')

readAndDisplay('Simulation.ReadValue_I2')
readAndDisplay('Simulation.ReadValue_I4')
readAndDisplay('Simulation.ReadValue_R4')
readAndDisplay('Simulation.ReadValue_R8')
readAndDisplay('Simulation.ReadValue_CY')
readAndDisplay('Simulation.ReadValue_DATE')
readAndDisplay('Simulation.ReadValue_BSTR')
readAndDisplay('Simulation.ReadValue_BOOL')
readAndDisplay('Simulation.ReadValue_DECIMAL')
readAndDisplay('Simulation.ReadValue_I1')
readAndDisplay('Simulation.ReadValue_UI1')
readAndDisplay('Simulation.ReadValue_UI2')
readAndDisplay('Simulation.ReadValue_UI4')
readAndDisplay('Simulation.ReadValue_INT')
readAndDisplay('Simulation.ReadValue_UINT')

readAndDisplay('Simulation.ReadValue_ArrayOfI2')
readAndDisplay('Simulation.ReadValue_ArrayOfI4')
readAndDisplay('Simulation.ReadValue_ArrayOfR4')
readAndDisplay('Simulation.ReadValue_ArrayOfR8')
readAndDisplay('Simulation.ReadValue_ArrayOfCY')
readAndDisplay('Simulation.ReadValue_ArrayOfDATE')
readAndDisplay('Simulation.ReadValue_ArrayOfBSTR')
readAndDisplay('Simulation.ReadValue_ArrayOfBOOL')
# readAndDisplay('Simulation.ReadValue_ArrayOfDECIMAL')
readAndDisplay('Simulation.ReadValue_ArrayOfI1')
readAndDisplay('Simulation.ReadValue_ArrayOfUI1')
readAndDisplay('Simulation.ReadValue_ArrayOfUI2')
readAndDisplay('Simulation.ReadValue_ArrayOfUI4')
readAndDisplay('Simulation.ReadValue_ArrayOfINT')
readAndDisplay('Simulation.ReadValue_ArrayOfUINT')

print()
print('Finished.')

##endregion Example
