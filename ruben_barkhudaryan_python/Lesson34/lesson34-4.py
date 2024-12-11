print("Working with files and folders")

import os

path = r"C:\Users\NPUA\Desktop\ruben_barkhudaryan_python"

for root, dir, files in os.walk(path):
    print("{0} has {1} files".format(root, len(files)))
