#!/usr/bin/env python
# coding: utf-8
1. Write a Python program to convert kilometers to miles?
2. Write a Python program to convert Celsius to Fahrenheit?
3. Write a Python program to display calendar?
4. Write a Python program to solve quadratic equation?
5. Write a Python program to swap two variables without temp variable?
# In[1]:


# 1. Write a Python program to convert kilometers to miles?

k = float(input("Enter the value in KM: "))
mi = k * 0.621371
print("The value in miles is: ", round(mi,2),"miles")


# In[2]:


# 2. Write a Python program to convert Celsius to Fahrenheit?

c = float(input("Enter the value in celsius: "))
f = c*1.8+32
print("The value in fahrenheit is: ", round(f,2))


# In[3]:


# 3. Write a Python program to display calendar?

import calendar

y = int(input("Enter the Year: "))

print(calendar.calendar(y))


# In[4]:


# 4. Write a Python program to solve quadratic equation?

import cmath

a = int(input("Enter the coefficient of x2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the value of Constant: "))

disc = (b**2) - (4*a*c)

x1 = (-b+cmath.sqrt(disc))/(2*a)
x2 = (-b-cmath.sqrt(disc))/(2*a)

print("The solutions are:",x1, "and" ,x2)


# In[5]:


# 5. Write a Python program to swap two variables without temp variable?

#Method1 - directly swap variables using assignment operator

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a,b = b,a

print("The value after swapping are a =",a, "and b =",b)

#Method2

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

x = x+y
y = x-y
x = x-y

print("The value after swapping are x =",x, "and y =",y)


# In[ ]:




