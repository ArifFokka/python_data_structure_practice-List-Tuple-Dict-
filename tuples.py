# Start Tuples
"""
my_tuple=1,2,4,5
print(my_tuple,type(my_tuple))
print(my_tuple[0:3]) #slic

empty_tuple=()
print(empty_tuple,type(empty_tuple))

cast_tuple=tuple([100,2,4,98]) #don't sord tuple
print(cast_tuple,type(cast_tuple))

cast_list=list(cast_tuple)
print(cast_list,type(cast_list))
"""
# Tuple problem solve
# 1. Write a Python program to create a tuple.
tuple=(1,2,3,'arif')
print(tuple,type(tuple))

# 2. Write a Python program to create a tuple with different data types
tuple=(1,2,3,'arif',5.55,6.44)
print(tuple,type(tuple))

# 3. Write a Python program to create a tuple with numbers and print one item.
tuple=(1,2,3,'arif',5.55,6.44)
print(tuple[0])

#4. Write a Python program to unpack a tuple in several variables
tuple=(1,2,3,5.55,6.44)
a,b,c,e,f=tuple
print(a,b,c,e,f) #helf code,

# 5. Write a Python program to add an item in a tuple
tuple=(1,2,3,5.55,6.44)
tuple=tuple + (7,8)
print(tuple)

#End problem solve of tuple