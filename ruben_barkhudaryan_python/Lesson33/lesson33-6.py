print("Working with files and folders")

with open(r"..\hello\hello.dat", "wb") as bin_file:
    bin_file.write(b"\x00\x00\xFF\xFF")

with open(r"..\hello\hello.dat", "r+b") as bin_file:
    print(bin_file.read())