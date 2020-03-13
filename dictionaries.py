# Start Dict

my_dict={}
print(my_dict)
my_dict=dict()
print(my_dict,type(my_dict))

my_dict={'one':1,'two':2,'three':3}
print(my_dict)
my_dict1={1:'one',1:'two'}
print(my_dict1[1])

#Key Dict True or False

print('one' in my_dict.keys(), 'Fokka' in my_dict )
print(1 in my_dict.values(), 3 in my_dict ) #Value not get without .value (but slow wordS)
print(my_dict.keys())
print(my_dict.values())

# Start problem solve of dict
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
dict={-1:'nage',10:1,9:"bbb",2:'ctc'}
p=sorted(dict.items())
m=sorted(dict.items(),reverse=True)
print('Ascending',p)
print("descending",m)


# 2. Write a Python script to add a key to a dictionary.
dict = {0: 10, 1: 20}
dict[2] = 30
print(dict)
dict.update({3:'last'})
print(dict)

#3. Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,1:60}
dic2.update(dic3)
dic1.update(dic2)
print(dic1)

#4. Write a Python script to check whether a given key already exists in a dictionary.
dict={1: 60, 2: 20, 3: 30, 4: 40, 5: 50}
key=dict.keys()
i=int(input('type num: '))
if i == key:
    print(i,"key already exists" )
else:
    print(i,"key  not exists" )

# 5. Write a Python program to iterate over dictionaries using for loops

dict= {1: 60, 2: 20, 3: 30, 4: 40, 5: 50}
for x in dict.items():
    print(x)

# end problem solve 
