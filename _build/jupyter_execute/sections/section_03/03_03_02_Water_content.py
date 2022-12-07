#!/usr/bin/env python
# coding: utf-8

# ## Normal Distribution
# ### Water content
# ---
# 
# <center><img title="a title" alt="Alt text" src="https://gitlab.tudelft.nl/prob-for-mude/examples/-/raw/main/Figures/Water_contet_normal.png" width="300" height="200" /></center>
# 
# Characterization of Eagle Ford Shale
# 
# According to [Characterization of Eagle Ford Shale](https://doi.org/10.1016/S0013-7952(02)00151-5),  the laboratory and field testing results of Eagle Ford Shale at the cancelled Superconducting Super Collider (SSC) project in Texas, USA. The Eagle Ford Shale has an average water content that can be generally considered to be normally distributed with a mean of 16% and a standard deviation of 2%.
# 
# 1. What value of water content is exceeded in 45 tests out of 50?
# 2. What is the probability that a clay sample picked at random has 15% of water content or less?
# 3. What is the probability that a clay sample picked at random has more than 18% of water content?
# 4. What is the probability that the water contents are in the range 15.5% -  17.5% ?
# 
# 
# 

# 1. What value of water content is exceeded in 45 tests out of 50?

# In[1]:


from scipy.stats import norm            #import normal function
p = 45/50
mu = 16
sigma = 2
water_content = norm.ppf(1-p,mu,sigma)  #norm.ppf is th percent point function (inverse of CDF).

#display the result rounded to two decimal places
print(f'{water_content:.2f}') 


# 2. What is the probability that a clay sample picked at random has 15% of water content or less?

# In[2]:


from scipy.stats import norm           #import normal function
mu = 16
sigma = 2
water_content = 15
probability  =  norm.cdf(water_content,mu,sigma) #norm.cdf is the CDF of the normal distribution

#display the result rounded to three decimal places
print(f'{water_content:.3f}') 


# 3. What is the probability that a clay sample picked at random has more than 18% of water content?

# In[3]:


from scipy.stats import norm           #import normal function
mu = 16
sigma = 2
water_content = 18
probability  =  1 - norm.cdf(water_content,mu,sigma) #norm.cdf is the CDF of the normal distribution

#display the result rounded to three decimal places
print(f'{water_content:.3f}') 


# 4. What is the probability that the water contents are in the range 15.5% -  17.5% ?

# In[4]:


from scipy.stats import norm  #import normal function
mu = 16
sigma = 2
water_content_i = 15.5
water_content_j = 17.7
probability  =  norm.cdf(water_content_j,mu,sigma) - norm.cdf(water_content_i,mu,sigma)

#display the result rounded to three decimal places
print(f'{water_content:.3f}') 


# In[ ]:




