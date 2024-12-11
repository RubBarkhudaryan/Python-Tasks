print("Math module")
print("Exercise 4 with excursion.")

def valueChecker():
    val = input("Enter value: ")
    if val == "":
        return
    else:
        print(val)
        valueChecker()
        
valueChecker()