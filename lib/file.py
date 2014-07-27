import lib
from lib import utils
from lib import audio
from lib import video
import mimetypes

mime_map = {
    "audio" : audio.assemblePath,
    "video" : video.process
}

def process(conf, full_path):
    
    mimetype = mimetypes.guess_type(full_path)
    type = mimetype[0].partition('/')[0]

    return mime_map[type](conf, full_path)

