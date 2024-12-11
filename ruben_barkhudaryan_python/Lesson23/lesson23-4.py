print("Data Types")
print("String")
print("String characters classification.")

str1 = "The pub is called 1 from 10"

str2 = "hello1234"

# if you use space symbol in string it will show false

print(str1.isalnum())
print(str2.isalnum())

str3 = "HalaMadrid"
print(str3.isalpha())
print(str3.isdigit())

str3 = "1234"
print(str3.isalpha())
print(str3.isdigit())

str5 = "this is 4"
print(str5.isdigit())

str1 = "my_var_2"
print(str1.isidentifier())

str1 = "class"
print(str1.isidentifier())

str2 = "2_my_var"
print(str2.isidentifier())
