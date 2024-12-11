#print("list")
#list1=["Aram",5.6,True,[1,3,5],15]
#print("using >0 index last element",list1[len(list1)-1])
#print("using <0 index first element",list1[-len(list1)])
##print("using <0 index last element",list1[-1])
#print(list1[3::])
#list1.append("lol")
#print(list1 )
##list1.insert(2,[1,"e",3.6])
#print(list1)
#list1.extend(["Hy","My",["By",1]])
#print(list1)
#list1.append(["lol",1])
#print(list1 )
print("assingn=")
#list1[1]=8
#print(list1)
print("slicing")
#list1[:]=["lol",2,7.5,5,6,5,223,36]
#list1[:2]=[45,2]
#print(list1)
#list1=[1,9,5,4,9,7]
#for i in range(len(list2)):
  #  square = list2[i]**2
   # list2[i]=square
#print(list2)
#for i in  list1:
 #     list1.remove(1)

#print(list1)
#list2.pop(3)
#print(list2)
#list2.clear()
#print(list2)


tup1=(1,2,3,2,4,2,6,7,4,2,4,5,1)
print(type(tup1))
position=tup1.index(2)
print(position)
position=tup1.index(2,2,5)
print(position)
position=tup1.index(2,10)
print(position)