print("Variables")

myFirstVariable = 5
camelCase = "camelCaseStyleVariable"
snake_case = "snake_case_variable"
PascalCase = "PascalCaseVariable"
CONSTANT_VARIABLE = 36.6

x, y, z = "one", "two", "three"

print(x, y, z)

print("Value swapping between variables non-traditional way")

num1 = 10
num2 = 20

print(num1, num2)

num1, num2 = num2, num1

print(num1, num2)


print("Value swapping between variables traditional way 1 - new variable for swapping")

num1 = 10
num2 = 20
temp = num1

print(num1, num2)

num1 = num2
num2 = temp

print(num1, num2)


print("Value swapping between variables traditional way 2 - ' nm+ -' operands")

num1 = 10
num2 = 20

print(num1, num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(num1, num2)
