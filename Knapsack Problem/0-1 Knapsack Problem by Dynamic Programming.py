#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter the number of items -> "))
sack = int(input("Enter the sack size -> "))


# In[2]:


class knapsack_object():
    def __init__(self, number, profit, weight):
        self.number = number
        self.profit = profit
        self.weight = weight


# In[3]:


def display_object(obj):
    for o in obj:
        print('object no. - ',o.number,' profit -',o.profit,' weight -',o.weight)


# In[4]:


obj = [knapsack_object(0,0,0)]
for i in range(n):
    print('--->for',i + 1,'instance')
    obj.append(knapsack_object((i + 1), int(input("Enter the profit -> ")), int(input("Enter the weight -> "))))
    print('-'*30)


# In[5]:


display_object(obj)


# In[17]:


def knapsack_dynamic_programming(table, obj, n, sack):
    for i in range(n + 1):
        for w in range(sack + 1):
            if i == 0 or w == 0: 
                table[i][w] = 0
            elif wt[i-1] <= w: 
                table[i][w] = max(val[i-1] + table[i-1][w-wt[i-1]],  table[i-1][w]) 
            else: 
                table[i][w] = table[i-1][w]
    return table            


# In[7]:


table = [[0] * (sack + 1)] * (n + 1)
table


# In[18]:


table = knapsack_dynamic_programming(table, obj, n, sack)


# In[14]:


table


# In[ ]:




