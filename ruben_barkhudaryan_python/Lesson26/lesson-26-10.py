print("Data Types")
print("Dictionaries")
print("Checking if a key exists in a dictionary")
dict1={'name':'Jessa','country':'USA','telephone':12345678,
       'weight':60,'height':6}
key_name='country'
if key_name in dict1.keys():
    print('country name is',dict1[key_name])
else:
    print('key not found')
