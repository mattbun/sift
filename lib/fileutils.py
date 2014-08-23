import shutil
import os
import errno

def mkdirsInPath(path):
    dirpath = os.path.dirname(path)
    try:
        os.makedirs(dirpath)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
            pass
        else:
            return 0

    return 1

def dryrun(source, destination):
    print(source + "\n\t-> " + destination)

def copy(source, destination):
    print(source)
    if (mkdirsInPath(destination)): #TODO rollback
        from shutil import copy
        shutil.copy(source, destination)
        print("\t-copied-to-> " + destination)

def move(source, destination):
    print(source)
    if (mkdirsInPath(destination)): #TODO rollback
        from shutil import move
        shutil.move(source, destination)
        print("\t-moved-to-> " + destination)


operation_map = {
    "move" : move,
    "copy" : copy,
    "dryrun" : dryrun,
    "test" : dryrun
}

def doSomethingWithFile(source, destination, operation):
    return operation_map[operation](source, destination)


