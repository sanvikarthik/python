#!/usr/bin/env python
# coding: utf-8

# In[2]:


m1=int(input("Enter text marks 1"))
m2=int(input("Enter text marks 2"))
m3=int(input("Enter text marks 3"))
best=0
if (m1>=m2):
    if(m2>=m3):
        best=m1+m2
    else:
        best=m1+m3
elif(m1>=m3):
    best=m2+m1
else:
    best=m2+m3
average=(best/2)
print("best of two is",average)


# In[ ]:


val=int(input("Enter number"))
strval=str(val)
if(strval==strval[::-1]):
    print("it is a pallindrome")
else:
    print("it is not a pallindrome")

for i in range (len(strval)):
    print(str(i),'appears',strval.count(str(i)))


# In[ ]:





# In[ ]:


val=int(input("Enter number"))
strval=str(val)
if(strval==strval[::-1]):
    print("it is a pallindrome")
else:
    print("it is not a pallindrome")

for i in range (len(strval)):
    print(str(i),'appears',strval.count(str(i)))


# In[ ]:




