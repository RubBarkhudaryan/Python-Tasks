print("Working with files and folders")
import os
import shutil

shutil.copy(
    r"C:\Users\NPUA\Desktop\hello\hello.txt", r"C:\Users\NPUA\Desktop\ruben_barkhudaryan_python"
)

print(os.listdir(r"C:\Users\NPUA\Desktop\ruben_barkhudaryan_python"))