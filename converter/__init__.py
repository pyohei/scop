"""Initial for converter operation.

This script is base of converter.
The selection of converter is created by this script.
"""

import os
import glob
import importlib 

# Ignore script as converter.
IGNORE_FILE = ['__init__']

def load_choices():
    """Load converter choices."""
    choices = []
    for f in glob.glob(os.path.dirname(__file__)+'/*.py'):
        c = os.path.basename(f).replace('.py', '')
        if c in IGNORE_FILE:
            continue
        choices.append(c)
    return choices

def convert(string, convert_type):
    """Execute convert.
    
    This module call convert module selected from choices.
    """
    module = importlib.import_module('converter.'+convert_type)
    return module.convert(string)
