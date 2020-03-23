# Usage: python3 list_python_modules.py 


#!/usr/bin/env python3


import sys
import pprint

print ("\n\n==================== python 3 modules ================================")
print ( help('modules'))			

print ("\n\n==================== python 3 Module Search Paths ====================")
pprint.pprint (sys.path)				
