#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


import pandas as pd


# In[4]:


base_site='https://www.firstnaukri.com/fnJobSearch/search'


# In[5]:


response=requests.get(base_site)


# In[6]:


response


# In[7]:


html=response.content
html


# In[8]:


soup=BeautifulSoup(html,'html.parser')
soup


# In[9]:


desc=soup.find_all('div',class_='tupple fn-card')


# In[10]:


desc


# In[13]:


jobtitle=[l.find('span',class_='elp').text for l in desc]


# In[14]:


jobtitle


# In[15]:


companyname=[l.find('span',class_='elp cName').text for l in desc]


# In[16]:


companyname


# In[17]:


salary=[l.find('span',class_='elp sal').text for l in desc]


# In[18]:


salary


# In[20]:


location=[l.find('span',class_='elp loc').text for l in desc]


# In[21]:


location


# In[22]:


qualification=[l.find('span',class_='elp txt').text for l in desc]


# In[23]:


qualification


# In[26]:


information=[l.find('span',class_='info-tag').text for l in desc]


# In[27]:


information


# In[28]:


df=pd.DataFrame()
df['job title']=title
df['company name']=companyname
df['qualification']=qualification
df['salary']=salary
df['location']=location
df['information']=information
df


# In[29]:


df.to_excel('job details first naukari.xlsx',index=False,header=True)


# In[ ]:




