import time
from sync.config import parse
from sync.sync_logic import sync_folders
from  sync.logger import Logger

def main():
    args = parse()
    logger = Logger(args.log_path)

    while True:
        sync_folders(args.source, args.replica, logger)
        time.sleep(args.interval)
if __name__ == "__main__":
    main()
