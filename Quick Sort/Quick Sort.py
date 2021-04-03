#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def random_array(n):
    minimum = int(input("Enter minimum number for random array -> "))
    maximum = int(input("Enter maximum number for random array -> "))    
    array = []
    for i in range(n):
        temp = random.randint(minimum, maximum)
        array.append(temp)
    return array 


# In[3]:


def partitioning(array,low, high):
    pivot = array[low]
    i = low
    j = high
    while i < j:
        while i < len(array) and array[i] <= pivot:
            i+=1

        while array[j] > pivot:
            j-=1
        
        if i < j: 
            array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low]
    return j


# In[4]:


def quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        j = partitioning(array, low, high)
        quick_sort(array, low, j - 1)
        quick_sort(array, j + 1, high)


# In[5]:


n = int(input("Enter the size of array -> "))
a = random_array(n)
a


# In[6]:


quick_sort(a, 0, len(a) - 1)
a


# In[7]:


sorted(a)

