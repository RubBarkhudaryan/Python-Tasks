print("Math module")
print("Exercise 2")

def sum_ints(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res
num=int(input("Enter an integer: "))
print(sum_ints(num))

    
