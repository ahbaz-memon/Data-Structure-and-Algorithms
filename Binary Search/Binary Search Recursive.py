#!/usr/bin/env python
# coding: utf-8

# In[20]:


import random


# In[22]:


def binary_search_recursive(array, key, low, high):
    if low == high:
        if array[low] == key:
            return low
        else:
            return None
    else:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            return binary_search_recursive(array, key, low, mid - 1)
        elif array[mid] < key:
            return binary_search_recursive(array, key, mid + 1, high)    


# In[13]:


def random_array(n):
    minimum = int(input("Enter minimum number for random array -> "))
    maximum = int(input("Enter maximum number for random array -> "))    
    array = []
    for i in range(n):
        temp = random.randint(minimum, maximum)
        array.append(temp)
    return array 


# In[17]:


n = int(input("Enter the size of array -> "))
k = int(input("Enter the key to search -> "))


# In[18]:


a = sorted(random_array(n))
a


# In[30]:


a = [1,6,2,4,5,12]
print("you search is at index no.",binary_search_recursive(sorted(a), k, 0, len(a)))


# In[ ]:




