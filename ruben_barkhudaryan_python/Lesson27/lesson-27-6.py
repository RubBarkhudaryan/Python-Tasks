print("Data Types")
print("Dictionaries")
print("Nested dictionary")
address={"state":"Texas","city":"Houston"}
person={"name":"Jessa","company":"Google","address":address}
print("person:",person)
print("City:",person['address']['city'])
print("Person details")
for key,value in person.items():
    if key=='address':
        print('Person Address')
        for nested_key,nested_value in value.items():
            print(nested_key,":",nested_value)
    else:
        print(key,":",value)
