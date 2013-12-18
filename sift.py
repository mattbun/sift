#!/usr/bin/python

import argparse
import configparser
import config
import os

import lib

def recurse(path, conf, assemblePath):
    from lib import fileutils
    for root, subFolders, files in os.walk(path):
        if '.AppleDouble' in subFolders:
            subFolders.remove('.AppleDouble')

        for folder in subFolders:
            recurse(os.path.join(root,folder), conf, assemblePath)

        for filename in files:
            original_path = os.path.join(root, filename)
            fileutils.doSomethingWithFile(original_path, assemblePath(conf, original_path), conf['file_operation'])

# Parse Arguments
parser = argparse.ArgumentParser(description='Move files based on perceived or existing metadata.')
parser.add_argument('--file', '-f', metavar='PATH', nargs=1, action='append', help='Sort a file/folder and let sift determine what type of file it is.')
parser.add_argument('--video', '-v', metavar='PATH', nargs=1, action='append', help='Sort file/folder as video')
parser.add_argument('--audio', '-a', metavar='PATH', nargs=1, help='Sort file/folder as audio')
args = parser.parse_args()

# Parse Configuration file
conf = config.config

if args.file is not None:
    from lib import file
    for f in args.file:
        recurse(f[0], conf, file.process)
        #print(file.process(conf, f[0]))

if args.audio is not None:
    from lib import audio
    for a in args.audio:
        recurse(a, conf, lib.audio.assemblePath)
        #print(lib.audio.process(conf, a))

if args.video is not None:
    from lib import video
    for v in args.video:
        recurse(v[0], conf, video.process)
        #print(video.process(conf, v[0]))

if args.video is None and \
   args.audio is None and \
   args.file is None:
    from lib import watch
    watch.start(conf) 


