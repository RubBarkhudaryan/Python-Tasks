print("Errors an exceptions")

a = [1, 2, 3]

try:
    print("First element", a[0])
    print("Second element", a[5])
except:
    print("Out of range")
