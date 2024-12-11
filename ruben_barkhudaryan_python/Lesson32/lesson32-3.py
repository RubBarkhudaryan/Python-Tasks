print("Working with files and folders.")

file = open(r"..\hello\hello.txt", "r+")

content = file.read()

print(content)

file.close()
