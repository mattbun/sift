from lib import utils
import mutagen

def assemblePath(conf, full_path):

    file_name = utils.getFileName(full_path)
    extension = utils.getExtension(full_path)
    containing_directory = utils.getContainingDirectory(full_path)

    tags = {
        'artist' : '',
        'album_artist' : '',
        'album' : '',
        'track_title' : '',
        'track_number' : '',
        'track_total' : '',
        'year' : '',
        'disc_number' : '',
        'disc_total' : '',
        'genre' : ''
    }
    #try:
    #    tags = getTags(extension, full_path, tags)
    #except mutagen.mp3.HeaderNotFoundError:
    #    print("No tags on this file")
    
    # hsaudiotag is pretty limited but it should at least let me get this project off the ground until I can figure out mutagen some more
    from hsaudiotag3k import auto
    
    fulltag = auto.File(full_path)
    if fulltag.valid:
       tags['artist'] = fulltag.artist
       tags['album'] = fulltag.album
       tags['track_title'] = fulltag.title
       tags['track_number'] = "%02d" % fulltag.track
       tags['year'] = fulltag.year
       tags['genre'] = fulltag.genre
    
    #print(tags)    

    result = conf['music_destination'] + utils.assemble(conf['music_format'], tags) + "." + extension
    return result

def getTags(extension, path, tags):
    if extension == "mp3":
        return getMP3Tags(path, tags)
    else: 
        return tags
   

def getMP3Tags(path, tags):
    from mutagen.mp3 import MP3
    from mutagen.easyid3 import EasyID3

    audio = MP3(path, ID3=EasyID3)

    tags['artist'] = audio['artist'][0]
    tags['album_artist'] = audio['performer'][0]
    tags['album'] = audio['album'][0]
    tags['track_title'] = audio['title'][0]
    tags['genre'] = audio['genre'][0]

    track = audio['tracknumber'][0].split('/')
    tags['track_number'] = track[0].zfill(len(track[1])) # TODO What if the track_total doesn't exist?
    tags['track_total'] = track[1]

    disc = audio['discnumber'][0]
    tags['disc_number'] = disc.split('/')[0]
    tags['disc_total'] = disc.split('/')[1]
    
    tags['year'] = audio['date'][0][:4]

    return tags



#
#    print("Artist: %s" % audio['artist'][0])
#    print("Album Artist: %s" % audio['performer'][0])
#    print("Album: %s" % audio['album'][0])
#    print("Title: %s" % audio['title'][0])
#    print("Track #: %s" % audio['tracknumber'][0])
    
    #print(audio.pprint())



#process("/home/matt/Music/2010 - Black City/01 - Honey.mp3")
