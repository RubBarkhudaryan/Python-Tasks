import os

print("Working with files and folders")

file = open(f"{os.getcwd()}/Lesson31/exFiles/example2.txt", "w")
file.write("Hello world")
file.close()
