print("Data Types")
print("Dictionaries")
print("Dictionary comprehension")
numbers=[1,3,5,2,8]
even_squares={x: x**2 for x in numbers if x%2==0}
print(even_squares)

telephone_book=[1178,4020,5786]
persons=['Jessa','Emma','Kelly']

telephone_dir={key: value for key,value in zip(persons,telephone_book)}
print(telephone_dir)
