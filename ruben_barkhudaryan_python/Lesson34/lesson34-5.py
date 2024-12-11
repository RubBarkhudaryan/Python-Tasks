print("Errors an exceptions")

marks = 10000

try:
    a = marks / 0
    print(a)
except ZeroDivisionError:
    print("Can't divide a number by zero.")