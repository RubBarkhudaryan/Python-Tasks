print("Data Types")
print("Dictionaries")
print("Python built-in functions - any()")
dict1={1:'aaa',2:'bbb',3:'AAA'}
dict2={0:12,0:13,2:14}
dict3={0:True,False:False}
dict4={}
print("All keys are true-",any(dict1))
print("One key is true-",any(dict2))
print("All keys are false-",any(dict3))
print("An empty dictionary-",any(dict4))
