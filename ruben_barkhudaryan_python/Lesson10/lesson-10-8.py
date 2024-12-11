print("Loops")
print("Functions")
print("Variable number of Arguments-keyword values")

def greet(name,msg):
    '''This function greets to
the person with the provided
message.

'''
    print("Hello",name+', '+msg)

greet(name="Bruce",msg="How do you do?")
greet(msg="How do you do?",name="Bruce")
greet("Bruce",msg="How do you do?")
