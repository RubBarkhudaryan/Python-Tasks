print("Data Types")
print("String")
print("Exercise 3")

str1 = "Day after day comes holiday"
str2 = list(str1)
value = str1[0]
new_str = value
for i in range(1, len(str1)):
    if str1[i].upper() == value.upper():
        str2[i] = "$"
    new_str += str2[i]
print(new_str)
