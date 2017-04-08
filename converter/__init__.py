"""Initial for converter operation."""
import os
import glob

IGNORE_FILE = ['__init__.py', '_sample.py']

def load_choices():
    choices = []
    for f in glob.glob(os.path.dirname(__file__)+'/*.py'):
        # TODO: Change it into generator.
        # print(f)
        choices.append(os.path.basename(f).replace('.py', ''))
    return choices


# print(load_choices())
