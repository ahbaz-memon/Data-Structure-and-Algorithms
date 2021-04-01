#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    for row in board:
        for e in row:
            print(e, end = '    ')
        print('\n')


# In[2]:


def is_safe(board, x, y, n):
    #upper column
    for row in range(x - 1, -1, -1):
        if board[row][y] == 1:
            return False
    
    # upper left diagonal
    row  = x - 1
    column = y - 1
    while row >=0 and column >=0:
        if board[row][column] == 1:
            return False
        row -= 1
        column -= 1
    
    # upper right diagonal
    row = x - 1
    column = y + 1
    while row >= 0 and column < n:
        if board[row][column] == 1:
            return False
        row -= 1
        column += 1
    
    return True


# In[ ]:


def n_queen(board, x, n):
    if x == n:
        return True
    for column in range(n):
        if is_safe(board, x, column, n):
            board[x][column] = 1
            if 


# In[3]:


n = int(input("Enter the number of Queen's for board -> "))


# In[4]:


board = [[0] * n] * n


# In[5]:


display_board(board)


# In[ ]:




