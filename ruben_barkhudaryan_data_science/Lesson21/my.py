#tup1=(1,2,[3,1,2],2,4,2,6,7,4,2,4,5,1)
#print(type(tup1))
#tup1[2][1]=60
#position=tup1.index(2)
#print(position)
#position=tup1.index(2,2,5)
#print(position)
#position=tup1.index(2,4)
#print(position)
#list1=list(tup1)
#list1[3]=10
#print(list1)
#for index in range(len(tup1)):
   # if type (tup1[index])==list:
    #    print("there is a list nested in", tup1,"under index,", index)
#print(tup1.count(2),tup1)
#import itertools
#tup1=(1,2,3,4,5)
#tup2=(7,8,9,8)
#tup3=tuple(item for item in itertools.chain(tup1,tup2))
#tup3=sum((tup1,tup2) ,())
#tup3=tup1+tup2
#print(tup3)
#tup2=tup1
#list2=list(tup2)
#list2.append(20)
#tup2=tuple(list2)
#print(tup1)
#print(tup2)##
tup1 =((1.3,2,4),(45,5),(3,2,1),False)
#print(tup1[3][1])
#for i in tup1:
 #   print("tuple",i,"element")
  #  for j in i:
   #     print(j,end=",")
    #print("\n")
#print(max(tup1))
print(any(tup1))
tup2=('Xaz',"aw","as","wsq")
print(max(tup2))