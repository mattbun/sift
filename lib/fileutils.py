
def doSomethingWithFile(oldpath, destination, format, data):
    from string import Template
    template = Template(format)

    newpath = destination + template.safe_substitute(data)
    print(newpath)

