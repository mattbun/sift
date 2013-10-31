import video, audio
import argparse
import configparser
import config

# Parse Arguments
parser = argparse.ArgumentParser(description='Move files based on perceived or existing metadata.')
parser.add_argument('--file', '-f', metavar='PATH', nargs=1, action='append', help='Sort a file/folder and let sift determine what type of file it is.')
#parser.add_argument('--video', metavar='PATH', dest='type_video', action='store_const', const=type_video, default=False, help='Process file/folder as video(s)')
parser.add_argument('--video', '-v', metavar='PATH', nargs=1, action='append', help='Sort file/folder as video')
parser.add_argument('--audio', '-a', metavar='PATH', nargs=1, help='Sort file/folder as audio')
args = parser.parse_args()

# Parse Configuration file
conf = config.config

if args.file is not None:
    for f in args.file:
        print(video.process(conf, f[0]))

if args.audio is not None:
    for a in args.audio:
        print(audio.process(conf, a))

if args.video is not None:
    for v in args.video:
        print(video.process(conf, v[0]))

