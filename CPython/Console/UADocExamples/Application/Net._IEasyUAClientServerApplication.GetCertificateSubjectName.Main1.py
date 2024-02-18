# $Header: $
# Copyright (c) CODE Consulting and Development, s.r.o., Plzen. All rights reserved.

##region Example
# Shows how to get the subject name of application certificates.
#
# Find all latest examples here: https://opclabs.doc-that.com/files/onlinedocs/OPCLabs-OpcStudio/Latest/examples.html .
# OPC client and subscriber examples in Python on GitHub: https://github.com/OPCLabs/Examples-QuickOPC-Python .
# The QuickOPC package is needed. Install it using "pip install opclabs_quickopc".
import opclabs_quickopc

# Import .NET namespaces.
from OpcLabs.EasyOpc.UA.Application import *
from OpcLabs.EasyOpc.UA.Application.Extensions import *


# Obtain the application interface.
application = EasyUAApplication.Instance

# Get the subject name of application certificates.
certificateSubjectName = IEasyUAClientServerApplicationExtension.GetCertificateSubjectName(application)

# Display results.
print('Certificate subject name: ', certificateSubjectName, sep='')

print()
print('Finished.')

##endregion Example
