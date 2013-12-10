#!/usr/local/bin/python3

import argparse
import configparser
import config
import os

import lib

def recurse(path, conf, process):
    for root, subFolders, files in os.walk(path):
        for folder in subFolders:
            if folder != '.AppleDouble':
                recurse(os.path.join(root,folder), conf, process)

        for filename in files:
            print(process(conf, os.path.join(root,filename)))

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
        recurse(a, conf, lib.audio.process)
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


