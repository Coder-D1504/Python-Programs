# Python Basic Functions
print("Hello World!")

print(len("Hello World!"))
print(sum([1,2,3,4,5,6,7,8,9,10]))
#User defined functions
def greet(name):
    return f"Hello,{name}!"
print(greet("Alcazar")) # Function Call
#Recursive Function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(10))
#Generator Function
def countdown(n):
    while n>0:
        yield n
        n-=1
for num in countdown(10):
    print(num)

#Multiline Comment
"""This is a multiline Comment
enjoy this code"""
# Variables
a,b,c=5,2.3,"Comment"
print("A = ",a,"B = ",b,"C = ",c)
print(type(a),type(b),type(c))
# Complex Values
a=5j+1
b=5j-1
print(type(a),type(b))

a,b=0,1
print(bool(a),bool(b))
c,d=True,False
print(type(c),type(d))

x=int(input("Enter String: "))
y=input("Enter String: ")
print(x)
print(y)
print(type(x),type(y))

x=None
print(type(x),x)

#List
x=[1,2,3,"Comment",True,None,"Star"]
print(x)
print(type(x))
print(type(x[0]),type(x[3]),type(x[4]),type(x[5]),type(x[6]))
print(x)
x[0]="HelloWorld"
print(x)

#Tuple
x=(1,"Hello",True)
print(x)
print(type(x))
# x[1]=x[3]
print(x[0:2])  #Slicing
print(x[:2])
print(x[:])
print(x[2:])

#Dictionary
dict={"Banana":"Calcium","Apple":"Health","CAR":"FORD GT"}
print(dict)
print(type(dict))
print(dict["Banana"])
print(dict.keys())
print(dict.values())

#Sets
s = {1,2,3,"Carbon",1.4,True}
print(s)
type(s)
empty={}
print(empty)

#Form
x=input("Enter NAME: ")
date=int(input("Enter Date: "))
month=int(input("Enter Month: "))
year=int(input("Enter Year:"))
print("Dear",x,",")
print("""Greetings from CSE Department!
I am delighted to inform you that you have been selected to participate in our Data
Analytics Bootcamp workshop.
Congratulations!
You are selected!
Have a great day ahead!
Thanks and regards,
CSE Department,
Indus University""")
print("Date:",date,"/",month,"/",year)
