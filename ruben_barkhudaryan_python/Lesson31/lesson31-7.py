print("Working with files and folders")

import os

path = r"C:\Users\NPUA\Desktop\hello\hello2.txt"

if os.path.exists(path):
    print("File already exists.")
else:
    with open(path, "w") as fp:
        fp.write("First line be like.")
