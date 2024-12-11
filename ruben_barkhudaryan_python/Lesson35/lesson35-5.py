print("Task 5\n")


def isPrime(num):
    prime = True
    rng = round(num**0.5)
    for i in range(2, rng + 1):
        if num % i == 0:
            prime = False
            break
    return prime


num = 1234

sum = str(num)

sum = int(sum[0]) + int(sum[len(sum) - 1])

print(f"The sum of number's number = {sum}, and the sum isPrime - ", isPrime(sum))
