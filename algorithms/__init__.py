"""
Initialisation file for all the algorithms contained in MSAF.
"""

__author__      = "Oriol Nieto"
__copyright__   = "Copyright 2014, Music and Audio Research Lab (MARL)"
__license__     = "GPL"
__version__     = "1.0"
__email__       = "oriol@nyu.edu"

import glob
import os

# Get current path
curr_path = os.path.dirname(os.path.realpath(__file__))
files = glob.glob(os.path.join(curr_path, "*"))

# Get all modules in the current path, which should be the algorithms
# available in MSAF
module_names = []
for file in files:
    if os.path.isdir(file):
        if os.path.isfile(os.path.join(file, "__init__.py")):
            module_names.append(__name__ + "." + os.path.basename(file))

# Import all the algorithms in this folder
[__import__(module_name, globals={}, locals={}, fromlist=[], level=-1)
 for module_name in module_names]

# Also init the __all__ var in case they want to use "*" to import all
__all__ = [module_name.split(".")[-1] for module_name in module_names]

# Clean up variable space
del curr_path
del files
del module_names
del os
del glob
del file
del module_name
