print("Task 4\n")


def isPrime(num):
    prime = True
    rng = round(num**0.5)
    for i in range(2, rng + 1):
        if num % i == 0:
            prime = False
            break
    return prime


i = 0
count = 0

while count <= 100:
    i += 1
    if isPrime(i):    
        count += 1
    
    
print(f"The 100th prime number is {i}")
