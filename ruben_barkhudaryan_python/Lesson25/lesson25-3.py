print("Data Types")
print("String")
print("Exercise 2")

str1 = "There are places I remember"
cnt = []
letters = []

for i in range(len(str1)):
    count = 0
    for j in range(i, len(str1)):
        if str1[i] == str1[j] and str1[i] not in letters:
            count += 1
    if(count):
        cnt.append(count)
        letters.append(str1[i])

zip1 = list(zip(letters, cnt))

print(zip1)