print("Data Types")
print("Dictionaries")
print("Add multiple dictionaries inside a single dictionary")
jessa={'name':'Jessa','state':'Texas','city':'Houston', 'marks':75}
emma={'name':'Emma','state':'Texas','city':'Dallas', 'marks':60}
kelly={'name':'Kelly','state':'Texas','city':'Austin', 'marks':85}

class_data={'student1':jessa,'student2':emma,'student3':kelly}
print(class_data)
print('Student 2 name:',class_data['student2']['name'])
print('Student 3 marks:',class_data['student3']['marks'])

print("\nClass details\n")
for key,value in class_data.items():
    print(key)
    for nested_key,nested_value in value.items():
        print(nested_key,':',nested_value)
    print("\n")
