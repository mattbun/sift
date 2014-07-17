import lib
from lib import utils
from lib import audio
from lib import video

extension_map = {
    "mp3" : audio.assemblePath,
    "avi" : video.process,
    "mkv" : video.process,
    "mp4" : video.process
}

def process(conf, full_path):
    extension = utils.getExtension(full_path)
    return extension_map[extension](conf, full_path)

