# def f(*n,name):
#     print("f :",n,name,)

# f(10,20,30,name="salman")

#keyword var len arg

# def mywish(**n):
#     print("information")
#     for k,v in n.items():
#         print(k,"......",v)

# display(name="aman",age=30,phn="9490")
# display(name="raju",age=34,phn="90")


# def f(arg1,arg2,arg3,arg4=6,arg5=9):
#     print(arg1,arg2,arg3,arg4,arg5)

# f(3,4,5)
# f(10,20,30,40)
# f(25,40,60,arg4=79)
# # f()
# f(arg2=78,arg3=67,arg4=89)
# f(36,78,arg3=78,arg5=67,arg4=89)

#function- A group of statements or instrution
#module - module is a file which contains a group of functions
#package - a folder which contains group of modules
#library - a group of packages is libaray


# def f1():
#     print("1")
# def f1():
#     print("1")
# def f1():
#     print("1")
# def f1():
#     print("1")


#types of variables

# a=1000
# def f():
#     print("f :",a)

# def f1():
#     b=200
#     print("f1 : ",a,b)

# f()
# f1()

#string data types

# s=input(" enter some word : ") #raju is a good boy 
# i=0
# for x in s:
#     print("the char present at positive index {} is {} and at negative index is {}".format(x,i,i-len(s)))
#     i+=1



#s[start index :end index:step] #end -1

# s="sunny bhai is good boy"

# print(s[-1:-7:-4])
# print(s[-1:-7:-4])
# print(s[-1:7:-3])
# print(s[-1:-7:-4])
# print(s[-1:-7:-4])
# print(s[-1:-7:-4])



# 2=1
# 3=2
# 4=3
# 5=4


#iterative statements-sometime a group of statements are requried to excute iterativly 

#for loop -for each element in squence
# do some actions
# #while loop


# s="sunny"
# for x in s:
#     print(x,end="")

#sunny

# s="sunny"
# count=0
# for i in s:
#     count+=1
#     print(i)
# print(" the number of char are ",count)

# s=input("enter some word") #raju
# i=0
# for x in s:
#     print("for each char present in ", i, "is" ,x)
#     i+=1
# # print("hello")

#prog  to print hello 10 times using for loop

# for i in range(10):
#    print("hello")

#pro 0-20 display only odd number to display

# for i in range(21):
#     if i%2==0:
#         print(i)


# l=[10,20,5,15,30]
# l1=list(filter(lambda x:x%2==0,l))   
# print(l1)


# 
# a=10
# def f1():
#     global a
#     a=11
#     print("f1",a)
#     print(globals())
#     print(globals()["a"])
# f1()
# def f2():
#     global a
#     a=222
#     print("f2",a)

# def f3():
#     print("f3",a)
# def f4():
#     print("f4",a)
# f1()
# f3()
# f2()
# f4()

# a=10
# a=10
# print(id(a))
# print(id(a))

#recursive functions
# n=5
# fact(n)=n*fact(n-1)
# fact(5)=5*fact(5-1)
# fact(4)=4*fact(4-1)
# fact(3)=3*fact(3-1)
# a=10
# print(id(a))

# l1=['A','B','C']
# l2=['A','B','C']
# print(l1 is l2)

# a=10
# b=10
# print(a == b)

# strip()


# city=input("enter the city name :") #mumbai
# l=["hyd is city","banglr","goa","delhi"]
# if city.strip() in l:
#     print("network is available at your city ")
# else:
#     print("sorry it is not avaiable")


#find() #it will give the frist occurence of a find value 

# s="this is aaaaaaman"
# print(s.find("boy"))
# #  if output == -1:
# # pass

# s="this is aaaaaaman"
# print(s.index("aman"))

# name=""
# password=""
# while (name!="raju") and (password!="123"): 
#     name=input("enter user name :")
#     password=input("enter the password :")
# print("hello ",name,"thank you for authentication")


#nested loops

# for i in range(4):
#     for j in range(4):
#         print("i={} and j={}".format(i,j))


# l1=[1,2,3,4]
# l2=[10,20,30,40]
# l3=list(map(lambda x,y:x*y,l1,l2))
# print(l3)
