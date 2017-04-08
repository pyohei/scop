"""Initial for converter operation."""
import os
import glob
import importlib 

IGNORE_FILE = ['__init__']

def load_choices():
    choices = []
    for f in glob.glob(os.path.dirname(__file__)+'/*.py'):
        # TODO: Change it into generator.
        # print(f)
        c = os.path.basename(f).replace('.py', '')
        if c in IGNORE_FILE:
            continue
        choices.append(c)
    return choices

def convert(string, convert_type):
    # TODO:
    #   - indicate converter directory with argument
    #   - error handling
    #   - testing code
    module = importlib.import_module('converter.'+convert_type)
    return module.convert(string)

# print(load_choices())
