#for increse the list : append(40),extend(),insert(1[60])
#to decrese : remove(specify element ),pop()

#reverse()
# l=["10","20","apple","Boy"] #unique code of upper case:97, Lower case:66
# l.sort(reverse=False)
# print(l)

# x=[10,60,30,40]
# y=x[:]
# y=x.copy()
# print(x)
# print(y)
# 

# a=[10,20,30]
# b=[40,50,60]
# c=a.extend(b) #none
# print(a)
# print(b)
# print(c)

# #comparing list object
# x=["Do","CaT"]
# y=["Dog","Cat"]
# z=['dog',"cat"]
# print(x==y)#True
# print(x==z)#false
# print(x!=z)#


# x=[50,90,60]
# y=[50,90,60,70,80]
# print(x>y)

# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# #elements row wise
# for r in x:
#     print(r)
#elemts in matrix style
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j], end=" ")
#     print()

#list comprehensive

# l=[1,4,9,16,25]

# l=[]
# for x in range(1,6):
#     l.append(x*x)
# print(l)

# l=[experssion for x in seq condition]
# l=[2**x for x in range(1,11) ]
# print(l)


#s[start index:end index] #end -1
# s="ramis boy"
# print(s[0:5])
# l=[10,20,30,40]
# print(l[2])

#bytes data type immuatble
# x={10,20,30,40}
# b=bytes(x)
# print(b)
# # for y in b:
# #     print(y)
# # print(b)
# # print(type(b))
# print(b[3])

#byte array data type #muteable 
# x=[10,40,20,30,60]
# # b=bytearray(x)
# # b[0]=130
# # for y in b:
# #     print(y)
# print(id(x))
# # print(b)

# x=10
# y=x
# print(id(x))
# print(id(y))


# l=[]
# # # print(l)
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# l.append(50)
# l.append(50)
# l.append(10)
# l.append("ramu")
# print(l)


#order is preserved
#duplicate values is allowed
#its growable in nature
#values should always be in close or square brakects []
#slice operator can be used in bases of indexing 

# s=[10,20,"aman","rgv",True]
# s1=s*2
# print(s1)

#tuple

# list=[10,20,30] #mutable    
# tuple=(10,20,30) #immuatble
# set={10,20,30} #mutable


# t=(10,20,"aman","ramu",10,20)
# # print(type(t))
# # print(t[0:3])
# t[0]=100
# print(t)

# t=(10,20,[30,40])
# print(t)

l=[x**2 for x in range(1,21)]








