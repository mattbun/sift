# utils.py - Functions that may need to be used anywhere in sift

import os
import string

# Take a format described by format and fill it with the data in values
def assemble(format, values):
    from string import Template
    template = Template(format)
    
    return template.safe_substitute(values)


# Removes leading and trailing whitespace and other characters that don't make sense to begin or end names (like hyphen)
def cleanString(str):
    str = str.strip();

# string.punctuation: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    start = 0
    for i in range(0, len(str) - 1):
        if (str[i].isspace() or \
            str[i] in string.punctuation):
            start = i
        else:
            break

    end = len(str)
    for j in range(len(str) - 1, 0, -1):
        if (str[j].isspace() or \
            str[j] == "-" or \
            str[j] == "."):
            end = j
        else:
            break

    return str[start:end]

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
