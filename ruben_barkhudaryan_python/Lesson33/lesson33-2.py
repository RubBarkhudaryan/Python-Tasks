print("Working with files and folders")
import os

def findFiles(filename, path):
    result = []
    for root, dir, files, in os.walk(path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

print(findFiles('hello.txt',r'C:\Users'))
