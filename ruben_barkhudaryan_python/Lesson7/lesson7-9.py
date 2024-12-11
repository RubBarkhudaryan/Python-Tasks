num = int(input("Input a 3 digits number: "))
a = num // 100
b = (num % 100) // 10
c = (num % 10) % 10

print(a, b, c)

digits = []

while num > 0:
    digits.append((num % 100)//10)
    num = num // 10

print(digits)
