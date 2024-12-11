print("Data Types")
print("Dictionaries")
print("Exercise 6 - Generate and print a dictionary that contains a number in the form (x,x^x)")

def gen_dict(num):
    keys=[]
    values=[]
    
    for i in range(1,num+1):
        keys.append(i)
        values.append(i*i)
    return dict(zip(keys,values))

num=int(input('Enter a number: '))

print(gen_dict(num))

