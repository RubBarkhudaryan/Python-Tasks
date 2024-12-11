print("\nLoops")
print()
print("While with else\n")

arr = [1, 2, 5, 4, 3, 6]
counter = 0

i = 1

while counter < 5:
    print("\nInside loop")
    if arr[counter] == 3:
        break
    else:
        print(arr[counter])
        counter += 1
        
# this else will not work if you break while loop faster than it needs

else:
    print("\nThe loop is over")
