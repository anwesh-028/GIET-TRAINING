'''#Function

def function1():
    print("it is the 1st function")
function1()
def function2(n1,n2):
    print("n1=",n1,"n2=",n2)
function2(10,20)
def function3(n4,n5):
    n6=n4+n5
    return n6
print(function3(100,200))


#categories
#based on argument
#positional argument

def function1(n1,n2,n3,n4):
    print("n1=",n1,"n2=",n2,"n3=",n3,"n4=",n4)
function1(10,20,30,40)


#keyword Arguments

def function2(n1,n2,n3,n4):
    print("n1=",n1,"n2=",n2,"n3=",n3,"n4=",n4)
function2(n1=10,n2=20,n3=30,n4=40)

#default arguments

def function3(name,rollno,branch,CollageName):
    print(name,rollno,branch,CollageName)
function3("Anwesh",28,"cse","Giet")

#variable no. of arguments

def function4(*var):
    for i in var:
        print(i,end=' ')

function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)


def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    print(sum1)

add(10,20)
print()
add(10,20,30,40)
print()
add(10,20,30,40,50,60)

#Q1.

a=int(input())
b=int(input())
c=int(input())

if a==7:
    print(b*c)
if b==7:
    print(c)
if c==7:
    print(-1)
else:
    print(a*b*c)

#Q2

a=float(input())
b=input("enter your currency name")
if b=="Euro":
    print(a*0.01417)
elif b=="British Pound":
    print(a*0.0100)
elif b=="Australian Dollar":
    print(a*0.02140)
elif b=="Canadian Dollar":
    print(a*0.02027)
else:
    print("-1")

#Q3

A=int(input("no. of Adults"))
C=int(input("no. of childs"))
ROA=float(37550.00)
ROC=float(37550.00/3)
RES=((A*ROA)+(C*ROC))+((A*ROA)+(C*ROC))*(7/100)
FIINALRES=RES-(RES*10/100)
print(FIINALRES)'''


#Q4
x=int(input("no. of 5 rupee coins"))
y=int(input("no. of 1 rupee coins"))
z=int(input("Amount"))
if(x * 5 + y < z):
    print(-1)
fives = min(x, z // 5)
ones = z - fives * 5
if(ones > y):
    print(-1)
else:
    print(fives, ones)



    









