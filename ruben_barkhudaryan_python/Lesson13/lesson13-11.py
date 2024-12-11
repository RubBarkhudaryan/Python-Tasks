print("Built-in functions.")
print(
    "Returning a list of results after applying the given function on a list of values."
)


def calculateAddition(n):
    return n + n


numbers = (1, 2, 3, 4)

result = map(calculateAddition, numbers)

print(set(result))
print(list(result))
