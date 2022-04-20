#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil
os.name


# In[3]:


filename = 'secret.txt'
print(os.path.join('/home/ammar/', filename))


# In[4]:


os.getcwd()


# In[6]:


os.mkdir('test')


# In[7]:


os.chdir('/home/mjams001/')


# In[8]:


if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print("the file is non existant")

