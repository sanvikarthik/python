#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PROG7B
class Employee:
    def __init__(self,Ename,Eid,Edept,Esal):
        self.name=Ename
        self.id=Eid
        self.dept=Edept
        self.sal=Esal
    def display(self):
        print(self.name,self.id,self.dept,self.sal)
    def update(self,dept,sal):
        if self.dept==dept:
            self.sal=sal
Emp=[]
n=int(input("Enter number of employees"))
for i in range(n):
    name=input("Enter employees name")
    eid=input("enter id")
    edept=input("enter dept")
    esal=input("Enter sal")
    emp1=Employee(name,eid,edept,esal)
    emp.append(emp1)
print("Employee details are")
for i in range(n):
    print(Emp[i].name," ",Emp[i].sal)
print("Update salary Particular Department")
dep=input("enter the department of the salary to be updated")
salary=int(input("Enter the salary to be upadated"))
for i in range(n):
    Emp[i].update_sal(dep,salary)
    print(Emp[i].name," ",Emp[i].sal)


# In[2]:


class PaliStr:
    def __init__(self):
        self.isPali = False

    def chkPalindrome(self, myStr):
        if myStr == myStr[::-1]:
            self.isPali = True
        else:
            self.isPali = False
        return self.isPali

class PaliInt(PaliStr):
    def __init__(self):
        self.isPali = False

    def chkPalindrome(self, val):
        temp = val
        rev = 0
        while temp != 0:
            dig = temp % 10
            rev = (rev*10) + dig
            temp = temp //10

        if val == rev:
            self.isPali = True
        else:
            self.isPali = False
        return self.isPali

st = input("Enter a string : ")

stObj = PaliStr()
if stObj.chkPalindrome(st):
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")

val = int(input("Enter a integer : "))    

intObj = PaliInt()
if intObj.chkPalindrome(val):
    print("Given integer is a Palindrome")
else:
    print("Given integer is not a Palindrome")


# In[3]:


#prog9
import requests
import os
from bs4 import BeautifulSoup

# Set the URL of the first XKCD comic
url = 'https://xkcd.com/1/'
# Create a folder to store the comics
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')

# Loop through all the comics
while True:
    # Download the page content
    res = requests.get(url)
    res.raise_for_status()

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')

        # Download the comic image
        print(f'Downloading {comic_url}...')
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the comic image to the xkcd_comics folder
        image_file = open(os.path.join('xkcd_comics', os.path.basename(comic_url)),'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    # Get the URL of the previous comic
    prev_link = soup.select('a[rel="prev"]')[0]
    if not prev_link:
        break
    url = 'https://xkcd.com' + prev_link.get('href')
print('All comics downloaded.')



# In[ ]:




