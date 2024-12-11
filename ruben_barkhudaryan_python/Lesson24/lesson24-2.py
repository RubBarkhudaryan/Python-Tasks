print("Data Types")
print("String")
print("Converting between strings and lists.")

list1 = ["one", "two", "three", "four", "five"]

str1 = ",".join(list1)

print(list1)
print(str1)
print(type(str1))

list2 = list(str1)
str1 = ",".join("python")
print(str1)

str1 = "how*happy*am*I"
print(str1.partition("*"))

str2 = "how much@@happy@@am I"
print(str2.partition("@@"))
print(str2.rpartition("@@"))

str1 = "what is love"
print(str1.rsplit())

str1 = "what*is*love"
print(str1.rsplit("*"))

str1 = "what is love baby don't hurt me"
print(str1.rsplit(maxsplit=2))
print(str1.split())
