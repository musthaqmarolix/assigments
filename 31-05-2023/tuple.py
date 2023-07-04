# x=[10,20,10]
# y=[10,10,30,50]
# print(x<y)

# l=[expression for in some sequnce condition]

# l1=[x*x for x in range(1,21)]
# l2=[x for x in l1 if x%2==0 ]
# print(l1)
# print(l2)

# l=[x for x in range(1,21) if x%2==0]
# print(l)

# l1=[x**2 for x in range(1,11) if x%2==0]
# print(l1)


# words=["venkateshwarlu","bindu","chiru","balakarishna"]
# l=[w for w in words if len(w)>5 ]
# print(l)

# "b","i","n","d","u"

# n1=[10,20,30,40]
# n2=[30,40,50,60]
# n3=[x for x in n1 if x not in n2]
# print(n3)

#tuple

#tuple is immutable
#only diff in list and tuple is mutable and immuatble rest of all its same as list 
#immutable is once value or elements or objects are given its fixed we cannot change 
#or it wont allow to performe any changes in the existing list
#insersation order is preserved 
# #list is also preserved
# duplicates are allowed both in tuple and list 
#tuple is read only version of list.
#indexing is allowed
#slicing is allowed

# t=10,20,30,40
# print(type(t))

# t=() #vaild
# t=10,20,30 #vaild
# t=10 #invalid 
# t=10, #vaild
# t=(10,) #vaild
# t=(10,20,30) #vaild


# list=[10,20,30]
# t=tuple(list)
# print(t)

# t=tuple(range(1,11))
# print(t)
# print(t[0])
# print(t[1:10:2])

# t=(10,20,30,40) #immutable
# # t[1]=123
# t1=(40,50,60)
# t2=t*2
# print(t2)

# l=[10,20,30]
# l1=l*3
# print(l1)

# s="boy"
# a=s*2


# n=[input("enter the input : ")]
# # l.split()
# # print(l)

# l=[eval(x.strip()) for x in n.split(",")]
# print(l)
# i= "10,20,a,b"

# values = i.split(",")
# print(values)

# result = []
# for i in l:
#     if type(i) == int:
#         result.append(i)
# total_sum = sum(result)
# print("Total sum of integer values:", total_sum)

# user_input = input("Enter a list of values, separated by commas: ")
# l = user_input.split(",")

# result = []
# for i in l:
#     if type(i) == int:
#         result.append(int(i))

# total_sum = sum(result)
# print("Total sum of integer values:", total_sum)

# user_input = input("Enter a list of values, separated by commas: ")
# l = [eval(x.strip()) for x in user_input.split(",")]

# result = []
# for i in l:
#     if type(i) == int:
#         result.append(i)

# total_sum = sum(result)
# print("Total sum of integer values:", total_sum)

#always index start=s from zero

# l=[10,"aman",True,10,20]
# # l1=l[1]
# print(l1)
# print(l)

# l[4]=100
# print(l)

#tuple
# t=()
# print(t)

# l=[]
# print(l)


#tuple is immuatble
#once elemts or object are given in tuple cannot be changed 
#or it wont allow to perform change
#tuple you can have duplicate elements
#tuple order is preserved 

# t=(10,20,30,40)
# t[0]=100
# print(t)

# t=(10,20,[10,30],50)
# print(t[2][0])

# range()

# a=range(0,-40)
# for x in a:
#     print(x)  #end value is -1

# user_input = input("Enter elements separated by spaces: ")
# elements = eval(user_input)

# integer_values = []
# for element in elements:
#     if type(element) == int:
#         integer_values.append(element)

# total_sum = sum(integer_values)
# print("Sum of integer values:", total_sum)

# input_list = input(" enter the input : ")
# values = input_list.split(",")
# print(values)
# result=[]
# con=[int(element) for element in values if element.isdigit()]
# print(con)
###values=['10','20','a','b',]
# result=[]
# for element in values:
#     if element.isdigit():
#         result.append(int(element))
#     elif element.replace('.', '', 1).isdigit():
#         result.append(float(element))  # Convert to float
# output=[]
# for i in result:
#     if type(i) == int:
#         output.append(i)

# total_sum = sum(result)
# print("Total sum of integer values:", total_sum)
# print(output)
# print(values)

# con=[elements for elements in values if elements.isdigit()]
# print(con)
# result = []

# for element in input_list:
#     if element.isdigit():
#         result.append(int(element))  # Convert to integer
#     elif element.replace('.', '', 1).isdigit():
#         result.append(float(element))  # Convert to float
#     else:
#         result.append(element)  # Keep it as a string

# print(result)

# i= "10,20,a,b"

# values = i.split(",")
# print(values)

# l = [10, 'a', True, 30, 'b', 40]
# result = []
# for i in l:
#     if type(i) == int:
#         result.append(i)

# total_sum = sum(result)
# print("Total sum of integer values:", total_sum)

# #10,20,a,b
# input_list = input("enter the input : ")
# value=input_list.split(",")

# com=[int(element) for element in value if element.isdigit()]

# # result=[]
# # for element in value:
# #     if element.isdigit():
# #         result.append(int(element))
# # # print(result)

# total_sum=sum(com)
# print(total_sum)


# k=input('ENTER ARRAY :')
# list = k.split(',')
# total = 0
# for i in list:
#     if i.isdigit():
#         total += int(i)

# print(total)


# result = []
# for i in l:
#     if type(i) == int:
#         result.append(i)
# total_sum = sum(result)
# print("Total sum of integer values:", total_sum)

# t1=(10,30,20)
# t2=(10,20,30)
# output=t1==t2
# print(output)

# l=[10,50,40,30]
# l.sort()
# print(l)

# t=(10,50,40,30)
# t.sort()
# print(t)

# t1='durgaA'
# print(min(t1))
# print(max(t1))


#dict get()

# d={100:"aman",200:"king fisher",300:10}
# print(d.setdefault(100,"mafia"))
# print(d)
# print(d.get(100))
# print(d.get(600,"bira"))
# print(d.values())
#item()
# dict([(100,valuman)
# l=d.items()
# # print(l)
# d1={10:"amma",20:"king ",30:20}

# d.update(d1)
# print(d)
# print(d1)

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(i,end="")
#     print()

# a=input("enter mobile number")
# b=a.split()
# print(b)
# # d=[]
# for x in range(1,100):
#     print(d.append)
#     if x in d:
#         pass
#     else: print("ticket number : ", x)

# s='hello world'
# l=s.split()
# print(' '.join(l[::-1]))

# s = 789765
# b= int(str(s)[::-1])
# print(b)

#nested loops

# for i range(5):
#     for j range(5):


# def f1():
#     print("aman")
# print(f1())

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# # x,y=sum_sub(100,200)
# c=sum_sub(100,200)
# print(c)
# # print("the sum",sum)
# # print("the sub :",sub)


#pro to display all the positions of sub string in the give main string
# s=input("enter the string :") #the boy name is ram
# subs=input("enter the sub string :")
# f=False
# pos=-1
# n=len(s)
# while True:
#     pos=s.find(subs,pos+1,n) #17
#     if pos==-1:
#         break
#     print("found at index : ",pos)
#     f=True
# if f==False:
#     print("not found ")


#s.replace
#syntax s.replace(oldstring,newstring)

# a="ram is very powerfull"
# b=a.replace("ram","ravi")
# print(a)
# print(b)

# s="abbabbabbbababababab"
# s=s.replace("a","b")
# print(s)

#split()
# s="10:20:30:40:50,:60,:70,40:50,:60,:70"
# l=s.split(",",3)
# print(l)
# # for i in l:
# #     print(i,end=" ")

#join()
#s=seprator.join(list)
# l=["ram","is","a","whiskey","boy"]
# s="".join(l)
# print(s)


