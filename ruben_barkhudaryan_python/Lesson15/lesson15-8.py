print("Built-in functions.")
print("Returning a zip object")

numList = [1, 2, 3, 4]
strList = {"1", "2", "3", "4"}
initials = ["name", "lastname", "proffesion"]
data = ["John", "Doe", "coder"]

result = tuple(zip(numList, strList))
print(result)

result2 = dict(zip(initials, data))
print(result2)
