import hashlib
import shutil

def get_file_hash(file_path):
    """  Take hash information"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

def copy(source, dest):
    shutil.copy2(source, dest)
