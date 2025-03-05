import os
import hashlib
import shutil

def get_file_hash(file_path: object) -> str:
    """  Take hash information"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

def copy(source, dest):
    shutil.copy2(source, dest)

def files_different(src, replica_file):
    if not os.path.exists(replica_file):
        return True
    src_stat = os.stat(src)
    replica_stat = os.stat(replica_file)

    if src_stat.st_size != replica_stat.st_size or int(src_stat.st_mtime) != int(replica_stat.st_mtime):
        return True
    return get_file_hash(src) != get_file_hash(replica_file)
