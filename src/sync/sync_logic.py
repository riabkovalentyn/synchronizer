import os
import concurrent.futures
from asyncio import tasks
from file_utils import files_different, get_file_hash, copy
from logger import Logger

def sync_folders(source, replica, logger):
    if not os.path.exists(replica):
        os.makedirs(replica)
        logger.log("Create folder:", replica)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        task = []

    for  root, files in os.walk(source):
        replica_root = root.replace(source, replica, 1)
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logger.log("Create folder:", replica_root)

        for file in files:
            src = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)

            if files_different(src, replica_file):
                tasks.append(executor.submit(copy, src, replica_file))
    concurrent.futures.wait(tasks)

    for root, files in os.walk(replica, topdown=False):
        source_root = os.path.join(source_root, file)

        for file in files:
            replica_file = os.path.join(root, file)


            for file in files:
                replica_file = os.path.join(root, file)
                if not os.path.exists(os.path.join(source_root, file)):
                    os.remove(replica_file)
                    logger.log("Delete dir:", replica_file)


