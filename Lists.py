
#start List code
'''
my_list=[]
print(my_list)
my_list=list()
print(my_list)

# Various type of data
my_list=[1,2,3,4,]
print(my_list)
my_list=['arif','bijoi','roni']
print(my_list)
my_list1=['arif',1,'roni',2.5]
print(my_list)

# 2 list add
add_list=my_list + my_list1
print(add_list,type(add_list))

# Empty and outher list add

empty_list=[]
my_list=[1,2,3,4,]
empty_list.extend(my_list)
print(empty_list,my_list)

# amny outher list add
my_list1=[1,2,3,4,]
my_list2=['arif','bijoi','roni']
my_list3=['arif',1,'roni',2.5]
my_list=my_list1 + my_list2 +my_list3
print(my_list)

# Sorting
my_list1=[1,2,3,4,80]
my_list1.sort()
print(my_list1[:])

#List End
'''

Start poblem solve of list
# List Problem Solve_1 (1. Write a Python program to sum all the items in a list)
list=[1,2,3]
i=0
for n in list:
    i+=n
print('the sum is :', i)

#2. Write a Python program to multiplies all the items in a list
list=[1,2,3,4]
i=1
for n in list:
    i*=n
print('the Mull is :', i)

#3. Write a Python program to get the largest number from a list
list=[40,2,3,4]
print(list)
list.sort()
print(list[:])
for n in list:
    pass
print('this it the largest num of list:',n)

# 4. Write a Python program to get the smallest number from a list.
list=[40,2,3,4]
print(list)
list.sort()
print(list[:])
for n in list:
    break
print('this it the Smallest num of list:',n)

# 5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

words=['abc', 'xyz', 'aba', '1221']
ctr = 0
for word in words:
    if len(word) > 2 and word[0] == word[-1]:
        ctr += 1
        print(word,ctr)

# help code this solution. but know Understands .
# End list problem solved.
