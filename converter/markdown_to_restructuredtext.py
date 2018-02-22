"""Convert markdown into reStructuredText"""
import pypandoc

def convert(string):
    return pypandoc.convert_text(string, 'rst', format='md')
