
import math


print("n")
print("range")
a=int(input("a="))
b=int(input('b='))   
c=int(input('c='))
if a>b: 
    max=a
    min=b
else:
    max=b 
    min=a
if c>max:
    print(min,max,c)
elif c<min:
    print(c,min,max)
else:
    print(min,c,max)


  