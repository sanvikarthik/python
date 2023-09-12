#!/usr/bin/env python
# coding: utf-8

# In[4]:


#prog6a
import sys
import os

fname=input("Enter file name")
if not os.path.isfile(fname):
    print("File does not exist")
    sys.exit(0)
infile=open(fname,'r')
Linelist=infile.readlines()
n=int(input("Enter number of lines to be read"))
for line in range(n):
    print(Linelist[line])
infile.seek(0)
word=input("enter word")
count=0
for line in Linelist:
    count+=line.count(word)
print("The word appears",count,"number of times")


# In[6]:


#prog6b
import os
import sys
import pathlib
import zipfile

userdirname=input("Enter user directory")
if not os.path.isdir(userdirname):
    print("Directory does not exist")
    sys.exit(0)

userdir=pathlib.Path(userdirname)

with zipfile.zipfile("myzip.zip",mode="w") as archive:
    for file_path in userdir.rglob("*"):
        archive.write(file_path,arcname=file_path.relativeto(userdir))
        
if os.path.isfile("myzip.zip"):
    print('zip file successfully created')
else:
    print('zip file not created')


# In[7]:


#prog6balternate
import os
import sys
import pathlib
import zipfile

dirName = input("Enter Directory name that you want to backup : ")

if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exists")
    sys.exit(0)
    
curDirectory = pathlib.Path(dirName)
    
with zipfile.ZipFile("C:\\Users\\deepa\\OneDrive\\Desktop\\xyz.zip", mode="w") as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curDirectory))
    
if os.path.isfile("ex.zip"):
    print("Archive", "myZip.zip", "created successfully")
else:
    print("Error in creating zip archive")


# In[11]:


#prog7a
import math
class Shape:
    def __init__(self):
        self.area=0
        self.name=""
    def showarea(self):
        print("The area of the ",self.name,"is",self.area)
class circle(Shape):
    def __init__(self,radius):
        self.area=0
        self.name="circle"
        self.radius=radius
    def calcArea(self):
        self.area=math.pi*self.radius*self.radius
class rectangle(Shape):
    def __init__(self,breadth,length):
        self.area=0
        self.name="rectangle"
        self.breadth=breadth
        self.length=length
    def calcArea(self):
        self.area=self.length*self.breadth
class Triangle(Shape):
    def __init__(self,height,base):
        self.area=0
        self.name="triangle"
        self.height=height
        self.base=base
    def calcArea(self):
        self.area=0.5*self.height*self.base
        
c1=circle(5)
c1.calcArea()
c1.showarea()
r1=rectangle(5,6)
r1.calcArea()
r1.showarea()
t1=Triangle(4,3)
t1.calcArea()
t1.showarea()


# In[ ]:




