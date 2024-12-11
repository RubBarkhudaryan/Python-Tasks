a = float(input("Insert number 1 : "))
b = float(input("Insert number 2 : "))
c = float(input("Insert number 3 : "))

max_ = 0
min_ = 0

if a >= b and a >= c:
    max_ = a
    
    if b <= c:
        min_ = b
    else: 
        min_ = c
        
elif b >= c and b >= a:
    max_ = b
    
    if a <= c:
        min_ = a
    else: 
        min_ = c
        
else:
    max_ = c
    
    if b <= a:
        min_ = b
    else: 
        min_ = a

print(f"Max = {max_}")
print(f"Min = {min_}")