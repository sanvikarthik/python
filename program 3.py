#!/usr/bin/env python
# coding: utf-8

# In[1]:


sent=input("Enter sentence")
num=0
u=0
lower=0
for i in range(len(sent)):
    if sent[i].isdigit():
        num=num+1
    elif sent[i].isupper():
        u=u+1
    elif sent[i].islower():
        lower=lower+1
    else:
        continue

print('this setence has',num,'digits',u,'upper case letters',lower,'lower case letters')


# In[ ]:


str1=input("Enter first string")
str2=input("Enter second string")
sim=0
if len(str1)<len(str2):
    length=len(str2)
else:
    length=len(str1)

for i in range(length):
    if(str1[i]==str2[i]):
        sim=sim+1
        
similarity=(sim/length)*100
print('',similarity)


# In[ ]:


str1=input("Enter first string")
str2=input("Enter second string")
sim=0
if len(str1)<len(str2):
    length=len(str2)
else:
    length=len(str1)

for i in range(length):
    if(str1[i]==str2[i]):
        sim=sim+1
        
similarity=(sim/length)*100
print('',similarity)


# In[ ]:




