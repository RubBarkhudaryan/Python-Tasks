print("Built-in functions")
print("Checking for true value in all values")
list1 = [1, 23, 4, 6, "hello", 12, True]
list2 = [1, 4, 6, True, 0, "False"]
list3 = [0, 0, False, "", 0]
list4 = []

# all - checks if all values in array are logically true

print("For all true values", all(list1))
print("For all true and one false values", all(list2))
print("For all false values", all(list3))
print("For an empty structure", all(list4))
