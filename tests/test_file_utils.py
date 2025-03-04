import os
import tempfile
from src.sync.file_utils import get_file_hash, copy

def test_get_file_hash():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test data")
        temp_file_path = temp_file.name

    try:
        hash1 = get_file_hash(temp_file_path)
        hash2 = get_file_hash(temp_file_path)
        assert hash1 == hash2, "Hash must match"
    finally:
        os.remove(temp_file_path)

def test_copy_file():
    with tempfile.NamedTemporaryFile(delete=False) as src_file:
        src_file.write(b"Test data")
        src_file_path = src_file.name

    dst_file_path = src_file_path + "_copy"

    try:
        copy(src_file_path, dst_file_path)
        assert os.path.exists(dst_file_path), "File must exist"
        assert get_file_hash(src_file_path) == get_file_hash(dst_file_path), "File must be same"
    finally:
        os.remove(src_file_path)
        os.remove(dst_file_path)