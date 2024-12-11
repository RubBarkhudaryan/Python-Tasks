print("Built-in functions.")
print("Filtering an object")


def filterdata(x):

    if x > 5:
        return x


result = filter(filterdata, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(tuple(result))
