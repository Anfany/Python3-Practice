
# coding: utf-8

# In[21]:


exdict = {1: [4, 7], 3:[5, 6]}


# In[22]:


# 键最大的,返回键和值
ckey = max(exdict.items(), key=lambda dw: dw[0])
print(ckey)


# In[23]:


# 值中第二个元素最大的,返回键和值
ckey = max(exdict.items(), key=lambda dw: dw[1][1])
print(ckey)


# In[24]:


# 值中元素乘积最小的,返回键和值
ckey = min(exdict.items(), key=lambda dw: dw[1][0] * dw[1][1])
print(ckey)

