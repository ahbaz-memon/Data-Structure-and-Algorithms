#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def binary_search_iterative(array, key):
    array = sorted(array)
    low = 0
    high = len(array)
    count = 0
    while low <= high:
        mid = (low + high) // 2
        print("iteration no. ",count," mid :",mid)
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            high = mid - 1
        elif array[mid] < key:
            low = mid + 1
        count += 1
    return None        


# In[3]:


def random_array(n):
    minimum = int(input("Enter minimum number for random array -> "))
    maximum = int(input("Enter maximum number for random array -> "))    
    array = []
    for i in range(n):
        temp = random.randint(minimum, maximum)
        array.append(temp)
    return array    


# In[4]:


n = int(input("Enter the size of array -> "))
k = int(input("Enter the key to search -> "))


# In[5]:


a = random_array(n)
a


# In[6]:


print("you search is at index no. ",binary_search_iterative(a, k))

