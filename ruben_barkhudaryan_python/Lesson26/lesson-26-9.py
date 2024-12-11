print("Data Types")
print("Dictionaries")
print("Removing items from a dictionary")
dict1={'name':'Jessa','country':'USA','telephone':12345678,
       'weight':60,'height':6}
deleted_item=dict1.popitem()
print(deleted_item)
print(dict1)
deleted=dict1.pop('country')
print(deleted_item)
print(dict1)

del dict1['weight']
print(dict1)
dict1.clear()
print(dict1)
del dict1
print(dict1)
