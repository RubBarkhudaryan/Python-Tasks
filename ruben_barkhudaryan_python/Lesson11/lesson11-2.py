print("\nLambda functions\n")

pow = lambda x: x**2

print(pow(3))


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_array = list(map((lambda x: (x % 2 == 0) and x * 2 or (x % 2 == 1) and x), array))

print(array)
print(even_array)
