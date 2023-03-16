'''#python programming

#datatypes
name="Anwesh"
print("name",name)
print("name",type(name))
rollno=28
print("roll no",type(rollno))
percentage=88.8
print("percentage",type(percentage))
complexnumber=3+6j
print("complexnumber",type(complexnumber))


#decision making statements

#1
n=int(input())
if(n%3==0):
    print("divisible by 3")
if(n%5==0):
    print("divisible by 5")
if(n%3==0 and n%5==0):
    print("divisible by both 3 and 5")
else:
    print("not divisible")



#Range function
#1 to 100
    

print("0 to 100")
for i in range(1,101):
    print(i,end=' ')
print()
print("0 to 100 even")
for i in range(0,101,2):
    print(i,end=' ')
print()
print("0 to 100 odd")
for i in range(0,101,3):
    print(i,end=' ')
print()
print("100 to 1")
for i in range(100,0,-1):
    print(i,end=' ')
print()
print("100 to 1 even")
for i in range(100,0,-2):
    print(i,end=' ')
print()
print("100 to 1 odd")
for i in range(99,0,-2):
    print(i,end=' ')



#break
for i in range(1,101):
    if i==50:
        break
    print(i,end=' ')
print()
print()
#continue
for i in range(1,101):
    if i==50:
        continue
    print(i,end=' ')
print()
print()
#pass
for i in range(1,101):
    if i==50:
        pass
    print(i,end=' ')'''







    


