#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program to square the elements of a list using map() function.


# In[1]:


def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Sample List: ",nums)
result = map(square_num, nums)
print("Square the elements of the list:")
print(list(result))

