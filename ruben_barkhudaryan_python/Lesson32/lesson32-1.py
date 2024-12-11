print("Working with files and folders.")

file = open(
    r"C:\Users\NPUA\Desktop\ruben_barkhudaryan_python\Lesson32\exFiles\example1.txt",
    "r",
)

content = file.read()

print(content)

file.close()
