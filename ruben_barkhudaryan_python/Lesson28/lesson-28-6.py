print("Data Types")
print("Dictionaries")
print("Exercise 4 - Check whether a given key already exists in a dictionary")
dict1={1:10,2:20,'hello':'good bye',5:12}
def key_exists(dictionary,key):
    keys=dictionary.keys()
    if key in keys:
        print('exists')
    else:
        print('does not exist')

key_exists(dict1,2)
key_exists(dict1,200)
