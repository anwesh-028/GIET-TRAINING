'''#List


list1=[]
print(list1,type(list1))

list2=[1,2,3,4,5]
print(list2)

list4=([1,2,3,4,5])
print(list4)

list5=[12,32,35,46,51]
print(list5)

list5.append(30)
print(list5)

list5.extend([21,33,30])
print(list5)

list5.insert(4,13)#add no. as per index(address,value)
print(list5)

list5.remove(35)#remove directly
print(list5)

list5.pop(3)#remove as per index
print(list5)





#Q1

def function(str):
    l_count=0
    d_count=0
    for i in str:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[ l_count, d_count]
print(function("infosys 123"))
print(function("ABC "))


#Q2
#addition of no. using pair.

def find_pair_of_numbers(list,n):
    count=0
    for i in list:
        index=list.index(i)+1
        for j in range(index,len(list)):
            if i+list[j]==n:
                count+=1
    return count
list=[1,2,3,4,5,6,0]
n=6
print(find_pair_of_numbers(list,n))
print(count(i,j))


#Q3


def function(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]
print(function("w3resource"))  


#Q4

def function(str1):
    if len(str1)<3:
        return str1
    elif(str1[-3:]=="ing"):
        return str1+"ly"
    else:
        return str1+"ing"
print(function("sleeping"))


#Q5

def function(num):
    num2=str(num*2)
    num=str(num)
    count=0
    for i in num:
        if i in num2:
            count+=1
        else:
            return False
    if len(str(num2))==len(str(num)):
        return True
    
print(function(2))
print(function(125874))

#Q6


lst_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    marks=0
    count=0
    for x in lst_of_marks:
        marks+=x
    average=marks/len(lst_of_marks)
    for x in lst_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(lst_of_marks)
    return percentage
def sort_marks():
    global lst_of_marks
    lst_of_marks=sorted(lst_of_marks)
    return lst_of_marks
def generate_frequency():
    freq=[]
    for x in range(26):
        count=0
        for y in lst_of_marks:
            if x==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())


#Q7

def translate(dictionary,txt):
    txt2=[]
    for i in txt:txt2.append(dictionary[i])
    return txt2
dictionary ={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
txt=["merry","christmas"]
print(translate(dictionary,txt))


#Q8
# Python 3 code to find count
# of sub-arrays with odd sum

def countOddSum(ar, n):
	result = 0

	for i in range(n):
		val = 0
		for j in range(i, n ):
			val = val + ar[j]
			if (val % 2 != 0):
				result +=1

	return (result)

ar = [ 5, 4, 4, 5, 1, 3 ]

print("The Number of Subarrays" ,"with odd", end = "")

print(" sum is "+ str(countOddSum(ar, 6)))'''


#Q8(2)

n1=int(input("Enter value of n1"))
n2=int(input("Enter value of n2"))
array=[i for i in range(n1,n2+1)]
print(array)
l1=[array[i:j+1] for i in range (len(array)) for j in range (i,len(array))]
print(l1)
c=0
for i in l1:
        if sum(i)%2!=0:
                c+=1
print(c)



 

    
    
















                
                
        





   
























      














      


