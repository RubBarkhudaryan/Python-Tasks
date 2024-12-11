print("Data Types")
print("Dictionaries")
print("Set default value to a key")
dict1={'name':'Jessa','country':'USA','telephone':12345678}
dict1.setdefault('state','Texas')
dict1.setdefault("zip")
dict1.setdefault('country','Canada')

for key,value in dict1.items():
    print(key,':',value)
