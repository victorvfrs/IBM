#!/usr/bin/env python
# coding: utf-8

# # <h1>My Jupyter Notebook on IBM Watson Studio<h1>

# **Victor Santiago** \
# Computer Engineering student

# *My interest in data science started with my curiosity about how we can extract a pattern based on some unconscious actions and use this information to generate the most varied insights*

# <h3>My code tests the bhaskara formula returning 0 if there is no real root<h3>

# In[7]:


import numpy as np
def bhaskara(a,b,c):
    delta = ((b**2) - (4*a*c))
    if(delta < 0):
        print("there is no real root")
        return 0
    else:
        x1 = ((-b + np.sqrt(delta))/(a*2))
        x2 = ((-b - np.sqrt(delta))/(a*2))
        return x1, x2
print(bhaskara(1,-25,100))


# 1. My numbered list
#     * My bullet list 
#         * My table:
#     <table>
#     <thead>
#     <tr>
#       <th>First Parameter</th>
#       <th>Second Parameter</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <td>name</td>
#       <td>age</td>
#     </tr>
#     <tr>
#       <td>Victor</td>
#       <td>28</td>
#     </tr>
#   </tbody>
# </table>
#     * Up level, again
# 2. Google link:
#     [Google](https://www.google.com/ "google.com")
# 3. Block quote:
#     >BLOCKQUOTE
# 4. ~~nevermind~~

# In[ ]:




