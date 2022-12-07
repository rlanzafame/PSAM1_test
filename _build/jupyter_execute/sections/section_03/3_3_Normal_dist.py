#!/usr/bin/env python
# coding: utf-8

# # Normal distribution
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Normal_dist.PNG" alt="" style="display: block; margin-left: auto; margin-right: auto;" width="400" height="230" /></p>
# 
# 
# Welcome to the Normal distribution module.  At the end of this module, you will be able to identify distribution parameters and evaluate probabilities for events using the Normal distribution. Manipulate the distribution parameters to evaluate conditions relevant to Civil Engineering and Geosciences (CEG) applications.
# 
# This module is set up with a 3-unit format:
# 
# 1. The basic theory of a specific concept.
# 2. Example of how a specific concept is applied to a  CEG problem, through step-by-step explanations and short python code blocks.
# 3. Introduction of a new problem, to practice using the method from unit 2.
# 
# ---
# ## 1. Theory
# 
# The Normal distribution is one of the most important distributions and is widely used in probability theory.  A continuous random variable X has a Normal distribution with parameters  $\mu$ (mean) and $\sigma$ (standard deviation) if its probability density function (PDF) is given by:
# 
# $f(x)=\frac{1}{\sigma \sqrt{2\pi }}\textrm{exp}\left [  {-\frac{1}{2}\left ( \frac{x-\mu }{\sigma } \right )^{2}}\right ] $
# 
# The cumulative distribution function (CDF) of the normal distribution can only be evaluated by numerical methods. In practice, one uses the standardized curve for the purpose of evaluation with the transformation of the variate X to Z as follows:
# 
# $ Z=\frac{X-\mu}{\sigma} $
# 
# Thus Z is Normal distribution with $\mu = 0$ and $\sigma = 1$ with PDF:
# 
# $f(z) = \frac{1}{\sigma \sqrt{2\pi }}\textrm{exp}\left [ {-\frac{z^2}{2}}\right ]$
# 
# Because of the symmetry of the PDF  $f(-z) = 1-f(z)$
# 
# 
# [Here](https://en.wikipedia.org/wiki/Standard_normal_table) you can find tables with numerical solutions of $F(z)$ and examples of how to use them. 
# 
# The distribution function of a Normal distribution has no closed form, however, it has been studied extensively. Almost every computer software and scientific calculator may return values for Normal distribution. 
# 
# ---
# 
# 
# ## 2. Water content
# 
# 
# <center><img title="a title" alt="" src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Water_contet_normal.png" width="300" 
#      height="200" /></center>
#      
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

# **1. What value of water content is exceeded in 45 tests out of 50?**
# 
# According to the laboratory results, the mean of the distribution is $\mu = 16$  and the standard deviation is $\sigma = 2$
# 
# We need to find the value of x which satisﬁes the condition:
# $ P(X>x) = 1 - F(x) = 1 - f(z) = \frac{45}{50} = 0.9 $
# 
# Thus, $ f(z) = 1-0.9=0.1 $
# 
# From the [Table](https://en.wikipedia.org/wiki/Standard_normal_table), $ z = -1.28 $ satisfies the condition.
# 
# From the equation $ z = \frac{x-\mu}{\sigma} $.
# 
# Solving for $x$, $ x = \mu +z \sigma  = 16 - 1.28(2) = 13.44 $
# 
# Hence, the water content is exceeded in 45 tests out of 50 is 13.44%
# 
# 
# We can easily obtain the solution using the following Python script:
# 

# In[1]:


from scipy.stats import norm            #import normal function
p = 45/50
mu = 16
sigma = 2
water_content = norm.ppf(1-p,mu,sigma)  #norm.ppf is th percent point function (inverse of CDF).

#display the result rounded to two decimal places
print(f'The water content is exceeded in 45 tests out of 50 is {water_content:.2f} %') 


# **2. What is the probability that a clay sample picked at random has 15% of water content or less?**
# 
# For the assumed mean = 16  and the standard deviation = 2
# 
# $P(X \leq 15) =  F(15) = F \left ( \frac{15-16}{2} \right )= F(-0.5)$
# 
# From the [Table](https://en.wikipedia.org/wiki/Standard_normal_table),  $ F(-0.5) = 0.3085 $
# 
# The probability that a clay sample picked at random has 15 \% of water content or less is 0.309
# 
# 
# We can easily obtain the solution using the following Python script:

# In[2]:


from scipy.stats import norm           #import normal function
mu = 16
sigma = 2
water_content = 15
probability  =  norm.cdf(water_content,mu,sigma) #norm.cdf is the CDF of the normal distribution

#display the result rounded to three decimal places
print(f'The probability that a clay sample picked at random has 15% of water content or less is  {probability:.3f}') 


# **3. What is the probability that a clay sample picked at random has more than 18% of water content?**
# 
# We can easily obtain the solution using the following Python script:

# In[3]:


from scipy.stats import norm           #import normal function
mu = 16
sigma = 2
water_content = 18
probability  =  1 - norm.cdf(water_content,mu,sigma) #norm.cdf is the CDF of the normal distribution

#display the result rounded to three decimal places
print(f'The probability that a clay sample picked at random has more than 18% of water content is {probability:.3f}') 


# **4. What is the probability that the water contents are in the range 15.5% -  17.5% ?**
# 
# For the assumed mean = 16  and the standard deviation = 2
# 
# $P(15.5 \leq X \leq 17.5) =  F \left ( \frac{17.5-16}{2} \right ) - F \left ( \frac{15.5-16}{2} \right ) $
# 
# By using the following Python script:

# In[4]:


from scipy.stats import norm  #import normal function
mu = 16
sigma = 2
water_content_i = 15.5
water_content_j = 17.7
probability  =  norm.cdf(water_content_j,mu,sigma) - norm.cdf(water_content_i,mu,sigma)

#display the result rounded to three decimal places
print(f'The probability that the water contents are in the range 15.5% -  17.5% is {probability:.3f}') 


# ---
# 
# ## 3.  Reinforcement bar tensile strength

# In[5]:


from IPython.display import HTML
import warnings
warnings.filterwarnings('ignore')

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/0ok09bucMXg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# The video that you saw is a steel reinforcing bar tensile strength test.  According to the laboratory test reported in the scientific publication ["Reliability analysis of reinforced concrete vehicle bridges columns"](https://doi.org/10.1016/j.engstruct.2019.03.011). The ultimate tensile strength $f_u$ of the steel bars in the study column, is described with a Normal distribution with a mean of 716.14 MPa and a standard deviation of 46.5 MPa.
# 
# **Please answer the following:**

# In[6]:


from jupyterquiz import display_quiz

display_quiz('quiz_3_3_3.json')

