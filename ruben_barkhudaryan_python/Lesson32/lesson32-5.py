print("Working with files and folders.")

count = 0

fp = open(r"..\hello\hello.txt", "r")

while True:
    count += 1
    line = fp.readline()

    if not line:
        break
    print("{}".format(line.strip()))

fp.close()
