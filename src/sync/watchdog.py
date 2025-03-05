from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from sync_logic import sync_folders
from logger import Logger

class SyncHandler(FileSystemEventHandler):
    def __init__(self, source, replica, logger):
        self.source = source
        self.replica = replica
        self.logger = logger

    def on_any_event(self, event):
        sync_folders(self.source, self.replica, self.logger)

def start_monitoring(source, replica, log_file):
    logger = Logger(log_file)
    event_handler = SyncHandler(source, replica, logger)
    observer = Observer()
    observer.schedule(event_handler, source, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()