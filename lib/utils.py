# utils.py - Functions that may need to be used anywhere in sift

import os

# Take a format described by format and fill it with the data in values
def assemble(format, values):
    from string import Template
    template = Template(format)
    
    return template.safe_substitute(values)


# Removes leading and trailing whitespace
# TODO MAKE THIS DO MORE THAN PYTHON'S STRIP FUNCTION
def cleanString(string):
    return string.strip()

# Pulls the filename from a path (no extension or folders)
def getFileName(path):
    containing, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    return name

# Pulls the containing folder from a path (no file name or extension)
def getContainingDirectory(path):
    containing, filename = os.path.split(path)
    return containing

# Pulls the extension from a path (no file name or folders)
def getExtension(path):
    name, ext = os.path.splitext(path)
    return ext[1:]
