print("Loops")
print("Functions")
print("Variables life scope")
x=20

def my_func():
    x=10
    print("Value inside the function:",x)
my_func()
print("Value outside the function",x)
