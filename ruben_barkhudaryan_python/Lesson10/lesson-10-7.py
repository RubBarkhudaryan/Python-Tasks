print("Loops")
print("Functions")
print("Variable number of Arguments-default values")
def greet(name,msg="Good morning!"):
    '''This function greets to
the person with the provided
message.
If the message is not provided,
it defaults to "Good morning"
'''
    print("Hello",name+', '+msg)

greet("Monica")
greet("Monica","How do you do?")


