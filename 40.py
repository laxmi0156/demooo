# 40)Write a Python program to get unique values from a list 

def fun(lst): 
    return list(set(lst)) 
my_list = [1, 2, 2, 3, 4, 4, 5, 1] 
print("Original list:", my_list) 
print("Unique values:", fun(my_list)) 
