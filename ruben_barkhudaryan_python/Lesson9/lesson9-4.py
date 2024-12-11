print("\nLoops")
print()
print("Loops with break and continue\n")

val = 5

for val in "Wednesday":
    if val == "n":
        break
    print(val)
else:
    print("The end\n")

print()

for val in "Wednesday":
    if val == "e":
        continue
    print(val)
else:
    print("The end")
