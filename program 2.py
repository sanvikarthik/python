#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n-1)+f(n-2)
    
num=int(input("Enter number"))
if(num>0):
    print('fibonacci of a number',num,'is',f(num))
else:
    print('error')


# In[4]:


def bintodec(b):
    return int(b,2)
def octtohex(o):
    return hex(int(o,8))

print('octal number:',end="")
onum=input()
hnum=octtohex(onum)
print("Equivalent hexadecimal value",hnum[2:].upper())
print("enter binary number:",end="")
bnum=input()
dnum=bintodec(bnum)
print("Equivalent decimal value",dnum)


# In[ ]:




