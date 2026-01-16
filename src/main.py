import os
import shutil
import sys
from copystatic import copy_contents
from generate_page import generate_pages_recursive  

dir_path_static = "./static"
dir_path_docs = "./docs"


def main():
    if len(sys.argv) > 2:
        print("cant have more than one args")
        raise Exception("too many args")
    basepath = "/"
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    print("deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("copying static files to public directory...")
    copy_contents(dir_path_static, dir_path_docs)
    
    generate_pages_recursive("./content", "./template.html", basepath)


# Update main.py: after copying files from static to public, it should generate a page from content/index.md using template.html and write it to public/index.html.
if __name__ == "__main__":
    main()
