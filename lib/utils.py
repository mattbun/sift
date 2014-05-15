# utils.py - Functions that may need to be used anywhere in sift

import os
import string

# Take a format described by format and fill it with the data in values
def assemble(format, values):
    format = scrubFormat(format, values)
    
    from string import Template
    template = Template(format)
    
    return template.safe_substitute(values)

# Remove fields that are null, clean up resulting format. This should make filepaths with 
# missing years, track numbers, etc. look nicer.
def scrubFormat(format, values):
    
    for tag in values:
        if (values[tag] == ''):
            format = format.replace('$' + tag, '')
    
    splitResult = []

    for pathElement in format.split('/'):

        start = 0
        for i in range(0, len(pathElement) - 1):
            if (pathElement[i].isspace() or \
                pathElement[i] == "-" or \
                pathElement[i] in string.punctuation):
                start = i
            else:
                break

        end = len(pathElement)
        for j in range(len(pathElement) - 1, 0, -1):
            if (pathElement[j].isspace() or \
                pathElement[j] == "-" or \
                pathElement[j] == "."):
                end = j
            else:
                break
        
        splitResult.append(pathElement[start:end])
   
    
#    str = str.strip();
    format = '/'.join(splitResult)

    return format.replace('//', '/') # It's possible that we may have made a null folder. Is that a thing?


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
