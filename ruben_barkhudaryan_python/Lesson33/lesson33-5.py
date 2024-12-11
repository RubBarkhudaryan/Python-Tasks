print("Working with files and folders")

with open(r"..\hello\hello.txt", "w") as file:
    file.write("Hello world!")

with open(r"..\hello\hello.txt", "r") as file:
    print(file.read())

with open(r"..\hello\hello.txt", "a") as file:
    file.write("\nThis is the second line.\n")

with open(r"..\hello\hello.txt", "r") as file:
    print(file.read())