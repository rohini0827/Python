#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assi 3
#create a python module with a function that calculates the area of a circle
#import this module in another script and use it to find the area for a radius of 5

import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = 5

area = area_of_circle(radius)

print(f"The area of a circle with radius {radius} is: {area:.2f}")


# In[2]:


#create a python function that imports datetime and returns the current date and time.

from datetime import datetime

def get_current_date_time():

    return datetime.now()

current_time = get_current_date_time()
print(f"Current date and time: {current_time}")


# In[3]:


#or
from datetime import *
print(datetime.now())


# In[4]:


#create a lambda function to check if a string starts with the letter 'A'

(lambda s: s[0].lower() == 'a')('Apple')


# In[5]:


#write a function that imports your custom module (e.g., math_utils.py) 
#and uses a function from it to calculate the factorial of a number


def factorial(n):
        
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)
        
factorial(5)


# In[6]:


#create a function that rounds a list of numbers to the nearest whole number

round_list = [4.5,2,3.8,5]
print(list(map(round,round_list)))


# In[7]:


#use round() inside map() to round a list of floating-point numbers to 1 decimal place.

round_list = [1.897,4.7864,2.654]
print(list(map(lambda n:round(n,1),round_list)))


# In[8]:


#write a function that takes two lists and uses map()to return a list of the sums  of corresponding elements
#example: add_lists([1, 2], [3, 4]) should return [4, 6].

print(list(map(lambda l1,l2:l1+l2,[1,2],[3,4])))


# In[ ]:




