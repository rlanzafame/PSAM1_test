#!/usr/bin/env python
# coding: utf-8

# # Geometric distribution
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/geometric_dist.PNG" alt="" style="display: block; margin-left: auto; margin-right: auto;" width="400" height="230" /></p>
# 
# 
# Welcome to the Geometric distribution module. At the end of this module, you will be able to identify distribution parameters and evaluate discrete probabilities for events using the Geometric distribution. Manipulate the distribution parameters to evaluate conditions relevant to Civil Engineering and Geosciences (CEG) applications.
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
# The geometric distribution is a discrete probability distribution where the random variable \( x \) indicates the number of Bernoulli trials required to get the first success (or failure). It is based on  the following three  assumptions:
# 
# 1. The trials being conducted are independent.
# 2. There can only be two outcomes of each trial - success or failure.
# 3. The success probability, denoted by p, is the same for each trial.
# 
# The probability mass function of the geometric distribution is given by
# 
# $p_{X}(x)=P(X=x)= p(1-p)^{x-1} \quad x=1,2,...$ 
# 
# ---
# 
# 
# ## 2. Water treatment plant failure assessment
# 
# 
# <center><img title="a title" alt="Culvert figure" src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Flocculator_tank.jpg" width="300" 
#      height="200" /></center>
#      
# 
# Suppose that it is known that the probability that the flocculator of a water treatment plant experiences a power failure in a given week is 15%. The manager of the water treatment plant would like to know:
# 
# 1. The probability that the flocculator will experience the first failure in exactly 4 weeks
# 2. The probability that the flocculator will experience the first failure in 4 weeks or less
# 3. The probability that the flocculator will experience the first failure in 4 weeks or more
# 

# **1. What is the probability that the flocculator will experience the first failure in exactly 4 weeks?**
# 
# 
# The probability of the flocculator experiencing a power failure in a given week is 15%, which means that $p =  0.15$.
# 
# 
# We're asked to solve the first failure in exactly 4 weeks. Therefore,  $x = 4$
# 
# 
# $ P(X=4) = 0.15(1-0.15)^{4-1}=0.092$
# 
# 
# Hence,  the probability that the flocculator will experience the first failure in exactly 4 weeks is 9.2%
# 
# 
# To answer this question we can use the following Python script:

# In[1]:


p = 0.15
x = 4
probability =  p*(1-p)**(x-1)

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}')


# 
# **2. What is the probability that the flocculator will experience the first failure will occur in 4 weeks or sooner?**
# 
# 
# We already know that  $p =  0.15$.
# 
# The probability that the first failure will occur in week 4 or sooner means that we need to solve $ P(X \leq 4) $. Therefore:
# 
# $P(X \leq 4) =\sum_{x=1}^{4}P(X=x)$
# 
# \begin{aligned} P(X \leq 4) &  = P(X=1)+P(X=2)+P(X=3)+P(X=4) \\& =  0.15(1-0.15)^{1-1} + 0.15(1-0.15)^{2-1}  \\ & \quad+ 0.15(1-0.15)^{3-1} + 0.15(1-0.15)^{4-1}  \\  &=  0.478  \end{aligned}
# 
# Hence,  the probability that the flocculator will experience the first failure will occur in 4 weeks or sooner is 47.8%
# 
# 
# To answer this question we can use the following Python script:

# In[2]:


p = 0.15
x = [1,2,3,4]
probability = sum([p*(1-p)**(week-1) for week in x])

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}')


# 3. What is the probability that the flocculator will experience the first failure in 4 weeks or more?
# 
# 
# We already know that  p =  0.15.
# 
# Now we need to solve \( P(X \geq 4) \). Therefore:
# 
# [mathjax] P(X \geq 4) = 1 -  P(X \leq 3)  = 1- \sum_{x=1}^{3}P(X=x)[/mathjax]
# 
# \begin{aligned} P(X \geq 4) &  = 1- \left [ P(X=1)+P(X=2)+P(X=3)  \right ] \\& =  1- \left [ 0.15(1-0.15)^{1-1} + 0.15(1-0.15)^{2-1}  0.15(1-0.15)^{3-1} \right ]  \\  &=  0.614  \end{aligned}
# 
# Hence,  the probability that the flocculator will experience the first failure in 4 weeks or more is 61.4%
# 
# 
# To answer this question we can use the following Python script:

# In[3]:


p = 0.15
x = [1,2,3]
probability = 1-sum([p*(1-p)**(week-1) for week in x])

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 

