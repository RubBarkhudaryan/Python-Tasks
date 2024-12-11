print("Data Types")
print("String")
print("Exercise 3")

str1 = "There are places"

str2 = ""

if len(str1) < 2:
    str2 = ""
else:
    str2 = str1[:2]
    str2 += str1[len(str1) - 2] + str1[len(str1) - 1]

print(str2)