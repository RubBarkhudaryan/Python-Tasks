print("Working with files and folders")

from datetime import datetime
import os


def createFile(path, file):
    if os.path.exists(path + file):
        print("File already exists.")
    else:
        with open(path + file, "w") as fp:
            print("File created - ", file)
            fp.write("First line be like.")


date = datetime.now()

path = r"C:\Users\NPUA\Desktop\hello\\"
file = date.strftime("%d-%m-%Y.txt")
createFile(path, file)

path = r"C:\Users\NPUA\Desktop\hello\\"
file = date.strftime("%d-%m-%Y-%H-%M-%S.txt")
createFile(path, file)
