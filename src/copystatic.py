import os
import shutil


def copy_files(cp_path, dst_path):

    if os.path.isfile(cp_path):
        print(f" * {cp_path} -> {dst_path}")
        shutil.copy(cp_path, dst_path)
    
    if os.path.isdir(cp_path):
        os.mkdir(dst_path)
    
    if os.path.isdir(cp_path):
        for path in os.listdir(cp_path):
            copy_files(
                os.path.join(cp_path, path),
                os.path.join(dst_path, path)
            )