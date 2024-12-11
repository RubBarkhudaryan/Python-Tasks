a = int(input("Insert number 1 : "))
b = int(input("Insert number 2 : "))
c = int(input("Insert number 3 : "))

count = 0

if a == 2:
    count += 1
if b == 2:
    count += 1

if c == 2:
    count += 1


if count == 2:
    print(True)
else:
    print(False)
