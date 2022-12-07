#!/usr/bin/env python
# coding: utf-8

# ## Uniform distribution
# ### Waiting time
# ---
# 
# 
# <center><img title="a title" alt="msc students" src="" width="300" 
#      height="200" /></center>
# 
# A master's student of TU Delft takes up a taxi to travel from home and university. The duration of the wait time of the taxi from the pickup point ranges from five to fifteen minutes.
# 
# 1. Plot the corresponding PDF and CDF graphs.
# 2. What is the probability that the student would have to wait exactly 5 minutes?
# 3. What is the probability that the student would have to wait at least 9.5 minutes?
# 4. What is the probability that a student would have to wait more than 5.8 minutes?
# 
# ---
# The probability density function (PDF) of the continuous uniform distribution is:
# $ f(x)=\left\{\begin{matrix}
# \frac{1}{b-a} & \mathrm{for} \, a\leq x\leq b, \\
# 0 & \mathrm{for} \, x < a \, \mathrm{or} \, x> b
# \end{matrix}\right.$
# 
# The cumulative distribution function (CDF) is: 
# 
# $ F(x)=\left\{\begin{matrix}
# 0 & \mathrm{for} \,  x < a \\
# \frac{x-a}{b-a} & \mathrm{for} \, a\leq x\leq b, \\
# 1 & \mathrm{for} \, x> b
# \end{matrix}\right.$
# 
# The mean or expected value of of the uniform distribution is given by: $ E\left [ X \right ] = \frac{b+a}{2 }$
# 
# The variance is: $ \mathrm{Var}\left [ X \right ] = \frac{(b-a)^{2}}{12 }$

# 1. Plot the corresponding PDF and CDF graphs.

# In[1]:


import numpy as np              #import python library numpy to use exponential
import matplotlib.pyplot as plt #matplotlib is a library for creating visualizations in Python

#interval [a,b]
a = 5
b = 15

x =  np.arange(0,20,.01)                     # Array of evenly spaced values

h = 1/(b-a)  # height of the distribution probability density function
f = [0 if j<=a or j>=b else h for j in x]   # probability density function (pdf)

plt.rcParams.update({'font.size':16})   # minimum font size is 16
plt.figure(figsize=(8,4))              # the figure size
plt.plot(x,f,'-', label=f'a = {a}, b = {b}')                       #label adds a legend in the plot    
plt.title('Probability density function', fontsize=20)
plt.grid('--',which='both',color='gray',alpha=.2)  #configure the grid lines
plt.xlabel('Minutes')                   #label of the x axis
plt.ylabel('f(x)')                      #label of the y axis
plt.legend()
plt.show()


# In[2]:


import numpy as np              #import python library numpy to use exponential
import matplotlib.pyplot as plt #matplotlib is a library for creating visualizations in Python

#interval [a,b]
a = 5
b = 15

x =  np.arange(0,20,.01)                     # Array of evenly spaced values
F = [0 if j<=a  else 1 if j>=b else (j-a)/(b-a) for j in x] # probability density function (CDF)

plt.rcParams.update({'font.size':16})   # minimum font size is 16
plt.figure(figsize=(8,4))               # the figure size
plt.plot(x,F,'-', label=f'a = {a}, b = {b}')         #label adds a legend in the plot    
plt.title('Cumulative distribution function', fontsize=20)
plt.grid('--',which='both',color='gray',alpha=.2)  #configure the grid lines
plt.xlabel('Minutes')                   #label of the x axis
plt.ylabel('F(x)')                      #label of the y axis
plt.legend()
plt.show()


# 2. What is the probability that the student would have to wait exactly 5 minutes?

# In[3]:


probability = 0

#display the result rounded to two decimal places
print(f'The probability is {probability:.2f}') 


# 3. What is the probability that the student would have to wait at least 9.5 minutes?

# In[4]:


#interval [a,b]
a = 5
b = 15
x = 9.5 
probability = (x-a)/(b-a)  #CDF

#display the result rounded to two decimal places
print(f'The probability is {probability:.2f}') 


# 4. What is the probability that a student would have to wait more than 5.8 minutes?

# In[5]:


#interval [a,b]
a = 5
b = 15
x = 5.8
probability = 1 - ((x-a)/(b-a))  #CDF

#display the result rounded to two decimal places
print(f'The probability is {probability:.2f}') 

