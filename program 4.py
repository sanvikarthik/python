#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

data=[]
length=int(input('Enter number of elements'))
print('enter elements')
for i in range(length):
    j=int(input())
    data.append(j)
insertionsort(data)
print('sorted array is ',data)


# In[11]:


#merge sort
def mergesort(arr):
    if(len(arr)<=1):
        return(arr)
    mid=(len(arr)//2)
    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=mergesort(left_half)
    right_half=mergesort(right_half)
    return merge(left_half,right_half)
def merge(left,right):
    merged=[]
    left_index,right_index=0,0
    
    while left_index<len(left) and right_index<len(right):
        if(left[left_index]<right[right_index]):
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

data=[]
length=int(input('Enter number of elements'))
print('enter elements')
for i in range(length):
    j=int(input())
    data.append(j)
sorted_list=mergesort(data)
print('sorted array is ',sorted_list)


# In[9]:


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  # Use integer division to get the midpoint
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = mergesort(left_half)  # Recursively sort the left half
    right_half = mergesort(right_half)  # Recursively sort the right half
    
    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements from left and right sides
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

data = []
length = int(input('Enter number of elements: '))
print('Enter elements:')
for _ in range(length):
    j = int(input())
    data.append(j)

sorted_list = mergesort(data)
print('Sorted array is:', sorted_list)


# In[ ]:


roman_numeral=input('enter roman number')
dict={'I':1,'V':5,'X':10,'L':50,'C':100,'M':1000}
result=0
for i in range(len(roman_numeral)):
    if i>0 and dict[roman_numeral[i]]>dict[roman_numeral[i-1]]:
        result+=dict[roman_numeral[i]]-2*dict[roman_numeral[i-1]]
    else:
        result+=dict[roman_numeral[i]]
print('',result)


# In[ ]:





# In[ ]:




