import random as rand

print("Data Types")
print("List")
print("Exercise 1")

even = []
odd = []

for i in range(10):
    num = int(input("Enter num : "))

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)
