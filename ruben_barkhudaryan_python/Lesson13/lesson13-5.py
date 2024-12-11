print("Built-in functions.")
print("Checking if the object is callable or not.")

num1 = 56
list1 = [1, 2, 3, 4, 5, 6]

def myFunc():
    return "Hello world"

print("Is a number type data callable ?", callable(num1))
print("Is a complex type data callable ?", callable(list1))
print("Is a function type data callable ?", callable(myFunc))
print("Is a built-in function callable ?", callable(callable))
