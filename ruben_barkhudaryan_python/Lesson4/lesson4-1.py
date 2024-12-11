print("Input, Output and Import")

a = 5
print(a)

print("Armen", 12, True, sep="*", end="###")
print("Second Line")


var1 = 10
var2 = 15

print("The value of var1 is {} and the value of var2 is {}.".format(var2, var1))
print("The value of var1 is {} and the value of var2 is {}.".format(var1, var2))
print("Car has an {} and {}.".format("engine", "transmission"))
print(
    "Car has an {1} and {0}.".format("transmission", "engine")
)  # {1}, {0} - format({0},{1}) - arguments

print("Car has an {e} and {t}.".format(t="transmission", e="engine"))
