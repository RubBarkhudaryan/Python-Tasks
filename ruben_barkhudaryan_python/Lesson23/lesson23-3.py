print("Data Types")
print("String")
print("String methods for find and replace.")

str1 = "This day is a special day, today is not like yesterday"

print(str1.count("day"))
print(str1.count("day", 7, 12))
print(str1.count("day", 0, 8))

print(str1.endswith("day"))
print(str1.endswith("day", 0, 8))
print(str1.endswith("day", 0, 9))

print(str1.find("day"))
print(str1.find("day", str1.find("day") + 1))

print(str1.find("special", 14))
print(str1.find("special", 15))

print(str1.index("like"))
# print(str1.index("Like")) ---> will show an error

print(str1.rfind("day"))
print(str1.rfind("day", 6, 30))

print(str1.rindex("day", 10, 30))

print(str1.startswith("day"))
print(str1.startswith("day", 5))
