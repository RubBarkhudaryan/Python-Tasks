print("Data Types")
print("Dictionaries")
print("Join two dictionaries using **kwargs")
dict1={'Jessa':50,'Kelly':60,'Anna':20}
dict2={'Harry':70,'James':55,"John":10}
dict3={'Paul':85,'George':40,'Richard':25}
new_dict={**dict1,**dict2,**dict3}
print(new_dict)
