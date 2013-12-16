# This is the configuration file for sift. Sift uses a python dictionary to hold 
# its configuration settings. If sift doesn't have a setting to handle a the
# file it's working on, it will just skip the file. So a good way to disable 
# certain types of files from being sifted is to leave the destination folder
# blank.

config = {
    'watch_directories': ['~/Music/Incoming', '~/Downloads'],
    'file_operation' : 'dryrun',

    'tv_format': '$show_name/Season $season_number/$show_name - S${season_number}E$episode_number - $episode_name',

    'music_format': '$album_artist/$year - $album/$track_number - $track_title',
    'music_destination': '~/Music'
}
