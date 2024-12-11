print("Working with files and folders")
import os

print(os.listdir(r"..\hello"))

os.remove(r"..\hello\05-06-2024-16-09-41.txt")

print(os.listdir(r"..\hello"))
