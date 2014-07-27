# utils.py - Functions that may need to be used anywhere in sift

import os
import string

# Take a format described by format and fill it with the data in values
def assemble(format, values):
    format = scrubFormat(format, values)
    
    from string import Template
    template = Template(format)
    
    return template.safe_substitute(values) + '.' + values["extension"]

# Remove fields that are null, clean up resulting format. This should make filepaths with 
# missing years, track numbers, etc. look nicer.
def scrubFormat(format, values):
    
    if (format.endswith(".$extension")):
        format = format[:-11]

    for tag in values:
        if (values[tag] == ''):
            format = format.replace('$' + tag, '')
    
    splitResult = []

    for pathElement in format.split('/'):
        splitResult.append(cleanString(pathElement))
   
    
#    str = str.strip();
    format = '/'.join(splitResult)

    return format.replace('//', '/') # It's possible that we may have made a null folder. Is that a thing?

# Clean up string
def cleanString(str):
    
    # Get rid of '()'
    str = str.replace('()', '')

    start = 0
    for i in range(0, len(str) - 1):
        if (str[i].isspace() or \
            str[i] == "-" or \
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

def isValidYear(year):
    import datetime
    if (year < (datetime.now().year + 10) and year > 1800):
        return 1
    else:
        return 0
