# 39)Write a Python program to find the second smallest number in a list. 

def fun(numbers): 
    unique = list(set(numbers))      
    unique.sort()                    
    if len(unique) < 2:         
        return "List doesn't have a second smallest number."     
    return unique[1]             
nums = [5, 2, 8, 1, 9, 2, 1] 
print("Original list:", nums) 
print("Second smallest number:", fun(nums)) 
