print("Conditionals")
print("nested conditional")
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print(num, " is zero")
    else:
        print(num, "is a positive number")
else:
    print(num, " is a negative number")
