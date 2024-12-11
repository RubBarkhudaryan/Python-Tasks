print("Errors an exceptions")


try:
    c = 5 / 0
    print(c)
except ZeroDivisionError:
    print("a/b result is 0")
finally:
    print("Hello world")
