print("Built-in functions")
print("Checking for true value in all values")
list1 = [1, 23, 4, 6, "hello", 12, True]
list2 = [1, 4, 6, True, 0, "False"]
list3 = [0, 0, False, "", 0]
list4 = []

# any - checks if any of values in array is logically true

print("For any true value", any(list1))
print("For any true and one false values", any(list2))
print("For any false values", any(list3))
print("For an empty structure", any(list4))
