import os
import tempfile
from src.sync.logger import Logger

def test_logger():
    with tempfile.NamedTemporaryFile(delete=False) as log_file:
        log_file_path = log_file.name

    try:
        logger = Logger(log_file_path)
        logger.log("Test log")

        with open(log_file_path, "r") as f:
            log_contents = f.read()

        assert "Test log" in log_contents, "Log must have some text data"
    finally:
        os.remove(log_file_path)