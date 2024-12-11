print("Loops")
print("Functions")
print("Variable number of Arguments-arbitrary values")

def greet(*names):
    '''This function greets all
persons in the names tuple.
'''
# names is a tuple with arguments
    for name in names:
        print("Hello",name)

greet("Monica","Luke","Steve","John")
 
