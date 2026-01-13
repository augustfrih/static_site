import shutil
import os

def copy_contents(static="./static", public="./public"):
    public_dir_abs = os.path.abspath(public)
    static_dir_abs = os.path.abspath(static)

    if not os.path.exists(public_dir_abs):
        os.mkdir(public_dir_abs)

    paths_to_copy = os.listdir(static_dir_abs)

    if len(paths_to_copy) != 0:
        for path in paths_to_copy:
            tmp_static = os.path.join(static_dir_abs, path)
            if os.path.isfile(tmp_static):
                shutil.copy(tmp_static, public_dir_abs)
            else:
                tmp_public = os.path.join(public_dir_abs, path)
                copy_contents(static=tmp_static, public=tmp_public)
