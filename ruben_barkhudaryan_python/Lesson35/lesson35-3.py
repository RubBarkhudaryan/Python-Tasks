print("Task 3\n")


def isPrime(num):
    prime = True
    rng = round(num**0.5)
    for i in range(2, rng + 1):
        if num % i == 0:
            prime = False
            break
    return prime


for i in range(10):
    print(f"{i} is a prime number - {isPrime(i)}")
