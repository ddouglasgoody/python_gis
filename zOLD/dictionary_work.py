
# coding: utf-8

# In[3]:


import datetime


# In[4]:


now = datetime.datetime.now()

print(now.year)


# In[6]:


import urllib.request
import json


# In[8]:


url = "https://data.cityofnewyork.us/resource/mzhu-ngrd.json"


# In[9]:


url


# In[10]:


with urllib.request.urlopen(url) as open_url:
    data = json.loads(open_url.read().decode())


# In[11]:


data


# In[12]:


data[0]


# In[13]:


data[10]


# In[20]:


for item in data:
    print(item['borough'])


# In[54]:


D = {}

for item in data:
    
    # ask does the borough exist in dictionary(D) 
    if item['borough'] not in D:
        D[item['borough']] = 1
    
    else:
        D[item['borough']] = D[item['borough']] + 1


# In[55]:


D

