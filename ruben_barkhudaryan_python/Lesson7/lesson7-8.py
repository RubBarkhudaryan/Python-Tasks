a = int(input("Insert number 1 : "))
b = int(input("Insert number 2 : "))
c = int(input("Insert number 3 : "))

max_ = a
mid_ = b
min_ = c

if a >= b and a >= c:
    max_ = a

    if b <= c:
        min_ = b
        mid_ = c
    else:
        min_ = c
        mid_ = b

elif b >= c and b >= a:
    max_ = b

    if a <= c:
        min_ = a
        mid_ = c
    else:
        min_ = c
        mid_ = a

else:
    max_ = c

    if b <= a:
        min_ = b
        mid_ = a
    else:
        min_ = a
        mid_ = b

print(f"Sorted elements {min_}, {mid_}, {max_}")
print(f"Sorted elements {max_}, {mid_}, {min_}")
