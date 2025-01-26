import os
import shutil
from copystatic import copy_files
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
path_template = "./template.html"
path_content_index = "./content/index.md"
path_public_index = "./public/index.html"

def main():
    public_exists = os.path.exists(dir_path_public)
    if public_exists:
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public)
        
    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)
    generate_page(path_content_index, path_template, path_public_index)
    

main()