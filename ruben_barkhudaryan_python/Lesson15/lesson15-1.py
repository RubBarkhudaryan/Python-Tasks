print("Built-in functions.")
print("Selecting the next element in the collection")

nums = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])

item = next(nums)
print(item)

item = next(nums)
print(item)

item = next(nums)
print(item)

print(list(nums))
