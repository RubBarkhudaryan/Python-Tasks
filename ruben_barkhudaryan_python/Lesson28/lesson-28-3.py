print("Data Types")
print("Dictionaries")
print("Exercise 1 - sort a dictionary by values")
dict1={1:'aaa',2:'bbb',3:'AAA',4:'xyz',5:'zara'}
def sort_by_value(d,reverse=False):
    return dict(sorted(d.items(),key=lambda x:x[1],reverse=reverse))

print(sort_by_value(dict1))
print(sort_by_value(dict1,reverse=True))       
