import os
import tempfile
import shutil
from src.sync.sync_logic import sync_folders
from src.sync.logger import Logger
from unittest.mock import MagicMock


def test_sync_folders():
    with tempfile.TemporaryDirectory() as source, tempfile.TemporaryDirectory() as replica:
        log_file = os.path.join(source, "test.log")
        logger = Logger(log_file)


        src_file = os.path.join(source, "test.txt")
        with open(src_file, "w") as f:
            f.write("Hello")

        logger = MagicMock()
        sync_folders(source, replica, logger)

        replica_file = os.path.join(replica, "test.txt")
        assert os.path.exists(replica_file), "Fime must  copy to  replica"


        with open(src_file, "w") as f:
            f.write("Updated")


        sync_folders(source, replica, logger)

        with open(replica_file, "r") as f:
            content = f.read()
        assert content == "Updated", " File in replica must be updated "


        os.remove(src_file)
        sync_folders(source, replica, logger)

        assert not os.path.exists(replica_file), "File must be deleted from replica"