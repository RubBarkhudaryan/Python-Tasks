print("Operators")
print("Special operators")
print("Identity operators")
x1 = 5
y1 = 5
print(id(x1))
print(id(y1))
var1 = id(x1)
print(var1)
print("x1 is y1 is", x1 is y1)
print("x1 is not y1 is", x1 is not y1)
x2 = "hello"
y2 = "hello"
print(id(x2))
print(id(y2))
print("x2 is y2 is", x2 is y2)
y2 = "Hello"
print("x2 is y2 is", x2 is y2)
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(id(x3))
print(id(y3))
print("x3 is y3 is", x3 is y3)
print("x3 is not y3 is", x3 is not y3)
