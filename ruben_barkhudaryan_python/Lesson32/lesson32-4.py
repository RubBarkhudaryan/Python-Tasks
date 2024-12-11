print("Working with files and folders.")

file = open(r"..\hello\hello.txt", "r+")

content = file.read(30)

print(content)

file.close()
