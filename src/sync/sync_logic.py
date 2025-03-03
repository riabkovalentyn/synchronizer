import os
import shutil
from file_utils import get_file_hash, copy
from logger import Logger

def sync_folders(source, replica, logger):
    if not os.path.exists(replica):
        os.makedirs(replica)
        logger.log(f"Create folder: {replica}")
    for  root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logger.log(f"Create folder: {replica_root}")

        for file in files:
            src = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)

            if not os.path.exists(replica_file) or get_file_hash(src) != get_file_hash(replica_file):
                copy(src, replica_file)
                logger.log(f"Copy/update file: {replica}")

    for root, dirs, files in os.walk(replica, topdown=False):
        rel_path = os.path.join(root, replica)
        source_root = os.path.join(source_root, file)

        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_root, file)

            if not os.path.exists(source_file) or get_file_hash(replica_file)!= get_file_hash(source_file):
                os.remove(replica_file)
                logger.log(f"Delete file: {replica_file}")
            for dir in dirs:
                replica_dir = os.path.join(root, dir)
                source_dir = os.path.join(source_root, dir)
                if not os.path.exists(source_dir)
                    logger.log(f"Delete dir: {source_dir}")


