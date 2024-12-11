print("Errors an exceptions")


def function_(a):
    if a < 4:
        b = a / a - 3
    print(f"b = {b}")


try:
    function_(3)
    function_(5)
except ZeroDivisionError:
    print("ZeroDivisionError occured")
except NameError:
    print("NameError occured")