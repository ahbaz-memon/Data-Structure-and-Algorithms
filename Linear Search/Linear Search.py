#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input("Enter the number of elements you want to keep in array -> "))


# In[5]:


A = []
for i in range(N):
    temp = int(input("Enter the element number " + str(i+1) + " -> "))
    A.append(temp)


# In[6]:


key = int(input("Enter the key which you want to search in array -> "))


# In[7]:


def Linear_Search(X, K):
    found = None
    for i in range(len(X)):
        if X[i] == K:
            found = i
            break
    return found


# In[ ]:


Linear_Search()

