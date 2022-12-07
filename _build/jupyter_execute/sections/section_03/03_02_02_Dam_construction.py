#!/usr/bin/env python
# coding: utf-8

# ## Exponential distribution
# ### Dam construction safety
# ---
# <center><img title="a title" alt="Culvert figure" src="https://gitlab.tudelft.nl/prob-for-mude/examples/-/raw/main/Figures/Dam_river_diversion.png" width="300" 
#      height="200" /></center>
# 
# A contractor is building a dam and river diversion is key to construction safety. The contractor is concerned about the possible occurrence of a flood exceeding 120 m3/s which can interrupt the construction. According to the records, a flow of such magnitude is exceeded once in 10 years on average. Assuming that the floods exceeding events are independent, identically distributed and can be modelled with an exponential distribution. The contractor would like to know: 
# 
# 1. What is the probability density function that describes the years between floods exceeding events?   
# 2. What is the chance that the construction will suffer interruptions in the first 2 years?
# 3. The construction of the bridge is scheduled to last 5 years. What is the probability that the work can be done without interruption because of the possible occurrence of a flood exceeding? 
# 
#  
# 

# 1. What is the probability density function that describes the years between floods exceeding events?   

# In[1]:


import numpy as np #import numpy library to use exponential function
import matplotlib.pyplot as plt #matplotlib is a library for creating visualizations in Python

Lambda = 1/10

plt.rcParams.update({'font.size':16})   # minimum font size is 16
plt.figure(figsize=(8,4))               # the figure size is 8 inches x 4 inches
x = np.arange(0,40)                     # Array of evenly spaced values
#plot of the pdf 
plt.plot(x,Lambda*np.exp(-Lambda*x), 
        label = f'$\lambda e^{{- \lambda x}}$, $\lambda$ = {Lambda}') #label adds a legend in the plot
plt.xlabel('Years')                     #label of the x axis
plt.ylabel('f(x)')                      #label of the y axis
plt.xlim([0,40])                        #limit of the x axis
plt.legend()                            #place the legend on the plot
plt.grid('--',which='both',color='gray',alpha=.2)  #configure the grid lines


# 2. What is the chance that the construction will suffer interruptions in the first 2 years?

# In[2]:


import numpy as np #import numpy library to use exponential function
Lambda = 1/10
x = 2
probability  =  1-np.exp(-Lambda*x)

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# In[3]:


import numpy as np #import numpy library to use exponential function
import matplotlib.pyplot as plt #matplotlib is a library for creating visualizations in Python

plt.rcParams.update({'font.size':16})   # minimum font size is 16
plt.figure(figsize=(8,4))               # the figure size is 8 inches x 4 inches
xx = np.arange(0,40)                     # Array of evenly spaced values
#plot of the cdf
plt.plot(xx,1-np.exp(-Lambda*xx), label = f'$ 1 - e^{{- \lambda x}}$, $\lambda$ = {Lambda}')
#plot of the 
plt.plot(x,probability,'ro', label = f'$P(X \leq {x})$ = {probability.round(3)} ' )

plt.xlabel('Years')
plt.ylabel('Cumulative probability')
plt.xlim([0,40])                        #limit of the x axis
plt.legend()                            #place the legend on the plot
plt.grid('--',which='both',color='gray',alpha=.2)  #configure the grid lines


# 3. The construction of the bridge is scheduled to last 5 years. What is the probability that the work can be done without interruption because of the possible occurrence of a flood exceeding? 

# In[4]:


import numpy as np #import numpy library to use exponential function
Lambda = 1/10
x = 10
probability  =  1-(1-np.exp(-Lambda*x))

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 

