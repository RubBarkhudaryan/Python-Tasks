print("Math module")
print("Exercise 3")

def sum_ints_rec(n):
    if n<=0:
        return 0
    else:
        return n+sum_ints_rec(n-1)

num=int(input("Enter an integer: "))
print(sum_ints_rec(num))
