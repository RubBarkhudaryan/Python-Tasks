import os

print("Working with files and folders")

os.mkdir(f"{os.getcwd()}/Lesson31/exFiles")
file = open(f"{os.getcwd()}/Lesson31/exFiles/example1.txt", "x")
file.close()
