print("Data Types")
print("Dictionaries")
print("Iterating a dictionary")
dict1={'name':'Jessa','country':'USA','telephone':12345678}
print('key',':','value')
for key in dict1:
    print(key,':',dict1[key])

print('key',':','value')
for key_value in dict1.items():
    print(key_value[0],':',key_value[1])
