a = int(input("Insert number 1 : "))
b = int(input("Insert number 2 : "))
c = int(input("Insert number 3 : "))

max_ = max(a, b, c)
min_ = min(a, b, c)
mid_ = 0

if max_ == a and min_ == b or max_ == b and min_ == a:
    mid_ = c
    
elif max_ == a and min_ == c  or max_ == c and min_ == a:
    mid_ = b
    
elif max_ == c and min_ == b or max_ == b and min_ == c:
    mid_ = a
    
d = max_ - mid_

print(f"max = {max_}, min = {min_}, mid = {mid_},  d = {d}")
    
if mid_ - min_ == d:
    print(True)
else:
    print(False)
