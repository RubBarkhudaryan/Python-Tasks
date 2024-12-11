print("Working with files and folders")

import os
import shutil

path_ = r"..\projects"

if os.path.exists(path_):
    shutil.rmtree(path_)
    print(path_ + " was removed")
