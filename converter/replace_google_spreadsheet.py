"""Sample convert."""


def convert(string):
    return string.rstrip('"').lstrip('"').replace('""', '"')
