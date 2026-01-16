import os
import shutil
from copystatic import copy_contents
from generate_page import generate_files_recursively  

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("copying static files to public directory...")
    copy_contents(dir_path_static, dir_path_public)
    
    generate_files_recursively("./content", "./template.html")


# Update main.py: after copying files from static to public, it should generate a page from content/index.md using template.html and write it to public/index.html.
if __name__ == "__main__":
    main()
