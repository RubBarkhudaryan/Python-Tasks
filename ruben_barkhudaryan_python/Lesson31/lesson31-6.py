print("Working with files and folders")

import os

path = r"C:\Users\NPUA\Desktop\hello"
file = "hello.txt"

with open(os.path.join(path, file), "w") as fp:
    fp.write("This is a new line!")
