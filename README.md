# sift (python edition)

**S**ift **I**sn't **F**or **T**orrenting

Sift is meant to automatically organize files on a computer based on filetype, metadata, and filename. It can be started as a daemon, where it watches a folder for changes, or it can be invoked from the command line with something like `sift /path/to/file`. It's meant to take as little user input as possible, besides the configuration file. Just give it a file to sort or a folder to watch, and sift will take care of it.

In particular, it focuses on organizing music, tv shows, and movies. For music, it relies on ID3 and vorbis tags. When it can't find that, it will attempt to pull that information from the file name and path. For tv and movies, it relies entirely on filename and path. For example, sift has no problem figuring out patterns like "/show name/Season 01/show name - S01E01 - episode name.mp4".

There are a couple other projects that are essentially predecessors to this version of sift.
 1. Matt's Music Manipulator (mmm) - A terrible program written way back after I had just started to learn Java. Full of spaghetti code, it just barely managed to organize a bunch of music files. No video support at all.
 2. Sift (written in Java) - less terrible but buggy, it supported both music and videos and even did external web lookups to tvdb.

This version of sift has been completely rewritten in Python and makes extensive use of regular expressions. It's much more stable and much better designed, but it's incomplete.
