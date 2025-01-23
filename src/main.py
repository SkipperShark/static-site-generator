import os
import shutil
from pprint import pp

# def get_all_paths(root_path):
#     if os.path.isfile(root_path):
#         return [root_path]
    
#     paths = []
#     for path in os.listdir(root_path):
#         new_path = os.path.join(root_path, path)
#         result = get_all_paths(new_path)
#         paths.extend(result)

#     return paths


def copy_items(cp_path, dst_path):
    print("-----")
    print(f"cp_path : {cp_path}, dst_path : {dst_path}")
    
    if os.path.isfile(cp_path):
        print(f"creating new file, copy_path : {cp_path}, dst_path : {dst_path}")
        return shutil.copy(cp_path, dst_path)
    
    # if os.path.isdir(cp_path):
    #     print(f"creating new dir with path {dst_path}/{cp_path}")
    #     os.mkdir(f"{dst_path}/{cp_path}")
    
    for path in os.listdir(cp_path):
        new_cp_path = os.path.join(cp_path, path)
        new_dst_path = os.path.join(dst_path, path)
        print(f"new_cp_path : {new_cp_path}, new_dst_path : {new_dst_path}")
        copy_items(new_cp_path, new_dst_path)
            
            
def static_to_public():
    path_to_public = "public"
    path_to_static = "static"
    public_exists = os.path.exists(path_to_public)
    if public_exists:
        shutil.rmtree(path_to_public)
        
    os.mkdir(path_to_public)
    # paths_to_copy = get_all_paths(path_to_static)
    # print(f"paths_to_copy : {paths_to_copy}")
    # for path in paths_to_copy:
    #     shutil.copy(path, path_to_public)

    copy_items(path_to_static, path_to_public) 


def main():
    static_to_public()
    
main()