#!/usr/bin/env python
# coding: utf-8

# ## Homogeneous Poisson distribution
# ### Reliability of equipment at a pump station
# ---
# 
# <center><img title="a title" alt="Pump figure" src="https://gitlab.tudelft.nl/prob-for-mude/examples/-/raw/main/Figures/Pumps.jpg" width="300" 
#      height="200" /></center>
# 
# All the pumps at a pump station have been made to the same specifications by a single manufacturer. From tests made over a 6-week period, it has been ascertained that there are on average two breakdowns during each period. It is assumed that the failures occur randomly in time, the occurrences are independent, and the rate of failure is constant.
# 
# 1. What is the probability that the water treatment plant will have exactly three breakdowns over 6 weeks?
# 2. A station manager assumes that the problem is not serious if there are no more than five breakdowns over 6 weeks. What is the probability of such an occurrence?
# 3. The water treatment plant would close for repairs if there are more than 7 breakdowns. The manager assumes that the probability of that happening is less than 0.10. Is this correct?
# 
# ---
# The homogeneous Poisson probability mass function (pmf) is given by:
# 
# $P(X=x)=\frac{\nu ^{x}}{x!}\mathrm{exp}(-\nu), \quad \nu=\lambda t  \quad x=0,1,2,...$
# 

# 1. What is the probability that the water treatment plant will have exactly three breakdowns over 6 weeks?

# In[1]:


import numpy as np  #import numpy library to use factorial and exponential functions
nu = 3
x = 2
probability = nu**x/np.math.factorial(x)*np.exp(-nu)

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# 2. A station manager assumes that the problem is not serious if there are no more than five breakdowns over 6 weeks. What is the probability of such an occurrence?

# In[2]:


import numpy as np #import numpy library to use factorial and exponential functions
nu  = 3
x = [0,1,2,3,4,5]
probability = sum([nu**breakdown /np.math.factorial(breakdown)*np.exp(-nu) 
                   for breakdown in x])

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}')                


# 3. The water treatment plant would close for repairs if there are more than 7 breakdowns. The manager assumes that the probability of that happening is less than 0.10. Is this correct?

# In[3]:


import numpy as np #import numpy library to use factorial and exponential functions
nu  = 3
x = [0,1,2,3,4,5,6,7]
probability = 1 - sum([nu**breakdown /np.math.factorial(breakdown)*np.exp(-nu) 
                       for breakdown in x])

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}')                       

