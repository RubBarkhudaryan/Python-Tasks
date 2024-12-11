a = int(input("Insert number 1 : "))
b = int(input("Insert number 2 : "))
c = int(input("Insert number 3 : "))
y = 1

if (a + b > c) and (a + c > b) and (b + c > a):
    y = 1
else:
    y = 2

print(f"y = {y}")
