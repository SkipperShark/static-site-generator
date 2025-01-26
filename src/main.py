import os
import shutil
from copystatic import copy_files_recursive
from generate_page import generate_page, generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
path_template = "./template.html"
path_content_index = "./content/index.md"
path_public_index = "./public/index.html"

def main():
    public_exists = os.path.exists(dir_path_public)
    if public_exists:
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public)
        
    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    # generate_page(path_content_index, path_template, path_public_index)
    generate_page_recursive(
        dir_path_content = dir_path_content,
        template_path = path_template,
        dest_dir_path = dir_path_public
    )

main()