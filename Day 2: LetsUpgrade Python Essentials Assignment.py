#!/usr/bin/env python
# coding: utf-8

# # List and its default functions.

# In[2]:


default_list=['ldygfdh', 123, 823247, 8273.0254, 'hjbff', True,[873, 'jfhkj', 873, 120.]]


# In[7]:


default_list.append(-1192)


# In[12]:


default_list


# In[13]:


default_list.remove(-1192)


# In[14]:


default_list


# In[19]:


default_list.index([873, 'jfhkj', 873, 120.0])


# In[33]:


default_list.pop(1)


# In[34]:


default_list


# In[48]:


default_list.insert(1, 23)


# In[49]:


default_list


# In[50]:


default_list.index(123)


# # Dictionary and its default functions.

# In[51]:


name = "Rony"


# In[52]:


age = 30


# In[53]:


has_android_phone = True


# In[54]:


name, age, has_android_phone


# In[55]:


person = {'Name': name, 'Age': age, 'HasAndroidPhone': has_android_phone}


# In[56]:


person


# In[57]:


type(person)


# In[58]:


person.keys()


# In[59]:


person.items()


# In[73]:


person.get("Name")


# In[71]:


person.values()


# In[74]:


person.pop("Name")


# In[75]:


person


# # Sets and its default functions

# In[77]:


set1={1,1,1,2,3,5,67,0,4,5,6,'asd','sdf','ssa','asd','er'}


# In[90]:


type(set1)


# In[78]:


set1


# In[79]:


set2={5,2,3,5,6,2,4,9,'asd','dsa'}


# In[80]:


set1.intersection(set2)


# In[81]:


set1.isdisjoint(set2)


# In[82]:


set2.issubset(set2)


# In[83]:


set2.issubset(set1)


# In[84]:


set1.issubset(set2)


# In[85]:


set1.intersection_update(set2)


# In[86]:


set1


# In[87]:


set2


# # Tuple and explore default methods.

# In[95]:


tup=(2, 3, 4, 5, 5, 6, 9, 'asd', 'dsa')


# In[89]:


type(tup)


# In[96]:


tup.count(5)


# In[97]:


tup.index(5)


# # Strings and explore default methods

# In[103]:


name = "Rony will be going today. Rony is leaving for Usa. Dont know when Rony will return"


# In[102]:


name.count('Rony')


# In[105]:


name.capitalize()


# In[106]:


name.swapcase()


# In[111]:


name.center(46)


# In[114]:


name.find('s')


# 

# In[115]:


name.islower()


# In[116]:


name.isupper()


# In[ ]:




