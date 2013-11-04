import os
from pyinotify import WatchManager, Notifier, ThreadedNotifier, EventsCodes, ProcessEvent

global_conf = None

class PTmp(ProcessEvent):
    def process_IN_CREATE(self, event):
        print("Create: %s" % os.path.join(event.path, event.name))
        #from lib import file
        #print(file.process(global_conf, os.path.join(event.path, event.name)))
    
    def process_IN_MOVED_TO(self, event):
        print("Moved: %s" % os.path.join(event.path, event.name))
        #from lib import file
        #print(file.process(global_conf, os.path.join(event.path, event.name)))

def start(conf):
    
    global_conf = conf

    wm = WatchManager()
    mask = EventsCodes.ALL_FLAGS['IN_CREATE'] | EventsCodes.ALL_FLAGS['IN_MOVED_TO']

    notifier = Notifier(wm, PTmp())
    
    for watch_dir in conf['watch_directories']:
        watch_dir = os.path.expanduser(watch_dir)
        print("Now watching %s" % watch_dir)
        wm.add_watch(watch_dir, mask, rec=True)

    while True:
        try:
            notifier.process_events()
            if (notifier.check_events()):
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break

