
'''#list comprehension
print([i for i in range(11)])
#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)



#odd numbers
print([i for i in range(11) if i%2!=0])
#odd numbers
result=[]
for i in range(11):
    if i%2!=0: 
        result.append(i)
print(result)




#even numbers
result=[]
for i in range(11):
    if i%2==0:
        result.append(i)
print(result)
#even numbers
print([i for i in range(11) if i%2==0])




#print odd and square evens
print([i  if i%2!=0 else i**2 for i in range(11)])
#print odd and square evens
result=[]
for i in range(11):
    if i%2==0:
        result.append(i**2)
    else:
        result.append(i)
print(result)



#print even and square odd
print([i  if i%2==0 else i**2 for i in range(11)])
#print even and square odd
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i**2)
    else:
        result.append(i)
print(result)




#for loop method
#odd-->square
#even-->cube
#in a given matrix
result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat2=[]
for row in mat:
    for element in row:
        mat2.append(element)
        if element%2!=0:
            result.append(element**2)
        else:
            result.append(element**3)
print(result)
#OR
result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat2=[element for row in mat for element in row]
for i in mat2:
    if i%2!=0:
        result.append(i**2)
    else:
        result.append(i**3)
print(result)


#list comprehension method
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([i**2 if i%2!=0 else i**3 for row in mat for i in row])
print([[i**2 if i%2!=0 else i**3 for i in row] for row in mat])




#Q1
#list comprehension method
mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
result =[(num,mylist.index(num)) for num in list_b if num in mylist]
print(result)
#for loop method
mylist = [9,3,6,1,5,0,8,2,4,7]
list_b = [6,4,6,1,2,2]
result =[]
for num in list_b:
    result.append((num,mylist.index(num)))
print(result)        


#extra

mylist = [9,9,3,6,1,5,0,8,2,4,7]
list_b = [6,9,4,6,1,2,2]
result =[(num,mylist.index(num)) for num in list_b if num in mylist]
result2= [(num,mylist.index(num)) for num, x in enumerate(mylist) if x == num in list_b]
print(result2)



#Q2

sentences = ["a new world record was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"
             ]

stopwords = ['for', 'was','a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
#for loop method
words = []
for sentence in sentences:
    sentence_words = sentence.split()           # Split the sentence into words
    for word in sentence_words:                 # Check if each word is a stop word or not
        if word not in stopwords:               # If the word is not a stop word, add it to the list of words
            words.append(word)

print(words)
#list comprehension method
words = [word for sentence in sentences for word in sentence.split() if word not in stopwords]
print(words) 

#Q3

input_str = "3,2,6,5,1,4,8,9"
num_list = [int(n) for n in input_str.split(',')]
pos_5 = num_list.index(5)
pos_8 = num_list.index(8)
# calculate sum of num1
num1 = sum(num_list[:pos_5]) + sum(num_list[pos_8+1:])
# calculate value of num2
num2 = int(''.join(map(str, num_list[pos_5:pos_8+1])))
print(num1+num2) '''

#Q4
#even rotate 1
#odd rotate 2
s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1, n =i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate (ss,n):
    n=str(n)
    s = 0
    for i in n:
        s+=int (i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range (len (numm)):
    print (rotate(stt[i],numm[i]))


























