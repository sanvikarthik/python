#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
def isphonenum(ph_num):
    if(len(ph_num)!=12):
        return False
    for i in range(len(ph_num)):
        if i==3 or i==7:
            if ph_num[i]!="-":
                return False
        else:
            if ph_num[i].isdigit==False :
                return False
    return True
def chkphonenum(ph_num):
    ph_num_pattern=re.compile(r'\d{3}-\d{3}-\d{4}$')
    if ph_num_pattern.match(ph_num):
        return True
    else:
        return False
ph_num=input("Enter phone number")
print("Without Regular Expression")
if(isphonenum(ph_num)):
    print("Valid phone number")
else:
    print("Invalid phone number")
print("With Regular Expression")
if(chkphonenum(ph_num)):
    print("Valid phone number")
else:
    print("Invalid phone number")
    


# In[ ]:




