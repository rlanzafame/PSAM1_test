#!/usr/bin/env python
# coding: utf-8

# # Binomial distribution
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/binomial_dist.PNG" alt="" style="display: block; margin-left: auto; margin-right: auto;" width="400" height="230" /></p>
# 
# Welcome to the Binomial distribution module. At the end of this module, you will be able to identify distribution parameters and evaluate discrete probabilities for events using the Binomial distribution. Manipulate the distribution parameters to evaluate conditions relevant to Civil Engineering and Geosciences (CEG) applications
# 
# This module is set up with a 3-unit format:
# 
# 1. The basic theory of a specific concept.
# 2. Example of how a specific concept is applied to a CEG problem, through step-by-step explanations and short python code blocks.
# 3. Introduction of a new problem, to practice using the method from unit 2.
# 
# ---
# 
# ## 1. Theory
# 
# The binomial distribution is used when there are two outcomes of a trial (success and failure). It is used to obtain the probability of observing x successes in N trials, with the probability of success on a single trial denoted by p. The binomial distribution assumes that p is fixed for all trials. In other words, it is useful for computing the probability of meeting a particular threshold given a specific error rate, and thus has applications to risk management. For this reason, the binomial distribution is also important in determining statistical significance.
# 
# It describes (pre-requisites):
# 
#    * Two outcomes per trial
#    * The probability of success (p) is the same across all trials
#    * The number of trials (n) is fixed
#    * Each trial is independent
# 
# The probability mass function of Binomial distribution for $x=0,1,...,n$ is:
# 
# $p_{X}(x)=P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}$
# 
# 
# ---
# 
# ## 2. Flood hazard assessment
# 
# 
# <center><img title="a title" alt="Culvert figure" src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Culvert.jpg" width="300" 
#      height="200" /></center>
# 
# Suppose that the annual maximum flood level in a drain channel has a probability of 0.02 of exceeding the design level of a culvert.
# 
# 1.	What is the probability that the design level of the culvert will be exceeded once in 50 years?
# 2.	What is the probability that it will be exceeded twice in 50 years?
# 3.	What is the probability that it will be exceeded in 50 years?
# 4.	What is the probability that it will be exceeded two or more times in 50 years?
# 
# 

# **1. What is the probability that the design level of the culvert will be exceeded once in 50 years?**
# 
# The most important part of this question is to realize that the answer is NOT 0.02! This may seem obvious right now, but it is a common mistake, since it is easy to associate the 50-year return period (that is, 1 / 0.02 = 50) to mean that the flood happens once in 50 years. Actually, the probability of exceeding the annual maximum flood level in one year is defined as 0.02, which is one of the parameters to use in our Binomial distribution, $p =  0.02$.
# 
# 
# We're asked to solve for once in 50 years. Therefore,  $x = 1$ and $n = 50$
# 
# 
# $ P(X=x) = \binom{50}{1}0.02^{1}(1-0.02)^{50-1}=0.372 $
# 
# 
# Hence,  the probability that the design level of the culvert will be exceeded once in 50 years is 37.2%
# 
# 
# To answer this question we can use the following Python script:

# In[1]:


from scipy.special import comb #import scipy.special library to use the combination function
p = 0.02
n = 50
x = 1
probability  = comb(n,x)*(p**x)*(1-p)**(n-x)

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# **2. What is the probability that it will be exceeded twice in 50 years?**
# Similarly that question 1. We're asked to solve for twice in 50 years. Therefore,  $x = 2$ and $n = 50$ and $p = 0.02$
# 
# 
# $P(X=x) = \binom{50}{2}0.02^{2}(1-0.02)^{50-2}=0.186 $
# 
# 
# Hence,  the probability that the design level of the culvert will be exceeded twice in 50 years is 18.6%
# 
# 
# To answer this question we can use the following Python script:

# In[2]:


from scipy.special import comb #import scipy.special library to use the combination function
p = 0.02
n = 50
x = 2
probability  = comb(n,x)*(p**x)*(1-p)**(n-x)

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# **3.  What is the probability that it will be exceeded in 50 years?**
# 
# Can you tell how this question is different from the first one? It's subtle, and has to do with the value of $x$. In this problem we are interested in one or more floods in 50 years, whereas in the first question we want to consider exactly one flood. So, $x\geq 1$ versus $x=1$. We can find this by summing up all possible values of $x$, but this is tedious, so we use the complement, $x=0$, which is much more simple, as shown below!
# 
# The probability that the culvert capacity will be exceeded is the same as 1 minus  the probability that it will not be exceeded. Hence, $x = 0$, $n = 50$ and $p = 0.02$.
# 
# 
# $ P(X=x) = 1-\binom{50}{0}0.02^{0}(1-0.02)^{50-0}=0.636 $
# 
# Hence,  the probability that the design level of the culvert will be exceeded  in 50 years is 63.6%
# 
# 
# To answer this question we can use the following Python script:

# In[3]:


from scipy.special import comb #import scipy.special library to use the combination function
p = 0.02
n = 50
x = 0
probability  = 1 - comb(n,x)*(p**x)*(1-p)**(n-x)

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# **4. What is the probability that it will be exceeded two or more times in 50 years?**
# 
# The probability that design level will be exceeded two or more times  $x \leq 2 $ in 50 years is the same as 1 minus the probability that design level be exceeded 0 or 1 times in 50 years. Hence $x_1 = 0$, $x_2 = 1$, $n = 50$  and $p = 0.02$
# 
# 
# $ P(X=x) = 1-\left [ \binom{50}{0}0.02^{0}(1-0.02)^{50-0}+\binom{50}{1}0.02^{1}(1-0.02)^{50-1}\right ]=0.264 $
# 
# Hence,  the probability that the design level of the culvert will be exceeded  two or more times in 50 years is 26.4%
# 
# 
# To answer this question we can use the following Python script:

# In[4]:


from scipy.special import comb #import scipy.special library to use the combination function
p = 0.02
n = 50
x1 = 0 
x2 = 1 
probability = 1 - ( comb(n,x1)*(p**x1)*(1-p)**(n-x1) 
            + comb(n,x2)*(p**x2)*(1-p)**(n-x2) )

#display the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 

