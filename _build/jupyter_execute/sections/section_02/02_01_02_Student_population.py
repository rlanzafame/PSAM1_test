#!/usr/bin/env python
# coding: utf-8

# # Bernoulli distribution
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/bernoulli_dist.PNG" alt="" style="display: block; margin-left: auto; margin-right: auto;" width="400" height="230" /></p>
# 
# Welcome to the Bernoulli distribution module. At the end of this module, you will be able to identify distribution parameters and evaluate discrete probabilities for events using the Bernoulli distribution. Manipulate the distribution parameters to evaluate conditions relevant to Civil Engineering and Geosciences  (CEG) applications
# 
# This module is set up with a 3-unit format:
# 
# 1. The basic theory of a specific concept.
# 2. Example of how a specific concept is applied to a CEG problem, through step-by-step explanations and short python code blocks.
# 3. Introduction of a new problem, to practice using the method from unit 2.
# ---
# ## 1. Theory
# 
# Bernoulli distribution
# 
# Let $ X $ be a discrete random variable with two possible outcomes, $x=0$ and $x=1$. The one and zero are arbitrary and used to represent the two possible outcomes in a simple way; sometimes one of these values also defined as failure. The Bernoulli distribution is commonly used when there are two outcomes of a trial (success or failure) and the probability of success is equal to $p$ (in this case we define success as $x=1$).
# 
# There are three important assumptions required to be able to apply the Bernoulli Distribution in practice:
# 
# * Each trial has exactly two possible outcomes
# * The probability of success (p) is the same across all trials
# * Each trial is independent
# 
# Based on these assumptions, we can write an equation that gives the probability of all possible outcomes of $x$ (there are only two!). Such an equation is called a probability mass function (PMF) because it describes how probability is allocated to all possible values of $x$. The PMF of the Bernoulli distribution is derived as a function of $x$ and $p$ as follows:
# 
# $p_{X}(x)=P(X=x)=p^x(1-p)^{1-x} \quad \textrm{for} \quad x = 0,1 $
# 
# where $p$ is the parameter that denotes the probability of a successful outcome. We can see that this PMF is quite simple for the Bernoulli case as $x$ can only take on a single value which simplifies the equation. The reason we write out the PMF here is because later we will see that the Bernoulli Distribution is a special case of the Binomial Distribution, specifically: the case of a single trial.
# 
# ## 2. Student population
# ---
# 
# 
# <center><img title="a title" alt="msc students" src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/02_01_02_Students.png" width="300" 
#      height="200" /></center>
# 
# According to TU Delft [Facts and Figures](https://www.tudelft.nl/en/about-tu-delft/facts-and-figures/), approximately 4 in 9 students are enrolled at the TU Delft master's program. One student is randomly selected.
# 
# 1. What is the distribution of the number of master's students?
# 2. What is the probability that we do get one master's student?
# 3. What is the probability that we do not get one master's student?
# 
# ---
# 
# 

# **1. What is the distribution of the number of master's students?**
# 
# We got a single trial, each student is a master's student, or they are not. Hence the conditions of a Bernoulli distribution here are satisfied. So the number of master's students is going to have a Bernoulli distribution with parameter $p =  4/9$.
# 
# If we let the random variable \(X\) be the number of master's students in our sample size 1. The distribution of the number of master's students is:
# 
# 
# $ P(X=x) = \left ( \frac{4}{9} \right )^{x}\cdot \left (1-\frac{4}{9}\right )^{1-x} $
# 
# for $x=0,1$ because we are gonna get a master's student  (1) or not (0).

# **2. What is the probability that we do get one master student?**
# 
# For this question 1 means that we do get one master's student i.e. $x=1$. If we substitute  $x=1$ in the previously obtained equation:
# 
# 
# $ P(X=x) = \left ( \frac{4}{9} \right )^{1}\cdot \left (1-\frac{4}{9}\right )^{1-1} =  \frac{4}{9} = 0.444$
# 
# 
# Hence, the probability that we do get one master's student is about 44.4%
# 
# 
# To answer this question we can use the following Python script:

# In[1]:


p = 4/9
x = 1
probability  = p**x*(1-p)**(1-x)

#displays the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# **3. What is the probability that we do not get one master's student?**
# 
# Here, do not get one master's student means that $x=0$. If we substitute  $x=0$ in equation obtained in question 1:
# 
# 
# $ P(X=0) = \left ( \frac{4}{9} \right )^{0}\cdot \left (1-\frac{4}{9}\right )^{1-0} =  \frac{5}{9} = 0.556$
# 
# 
# Hence, the probability that we do not get one master's student is about 55.6%
# 
# 
# To answer this question we can use the following Python script:

# In[2]:


p = 4/9
x = 0
probability  = p**x*(1-p)**(1-x)

#displays the result rounded to three decimal places
print(f'The probability is {probability:.3f}') 


# ---
# That's it! Note that this was a pretty simple set of exercises because the Bernoulli is a very simple distribution. We used the PMF to make our calculations, but you should also be able to go back and see how the answers could have been determined directly using the ratio of master's students in each case. 
# 
# Now let's test this knowledge on a new problem!
# 
# ---
# 
# ## 3. International master's student population
# 
# According to TU Delft [Facts and Figures](https://www.tudelft.nl/en/about-tu-delft/facts-and-figures/), the total student population enrolled at the TU Delft master's program is 13029 of which 4356 are international students.  One master's student is randomly selected.
# 
# Please answer the following:
# 

# In[3]:


from jupyterquiz import display_quiz

display_quiz('quiz_2_1_3a.json')


# The following plots show three Bernoulli probability mass functions of the number of international master's students:
# 
# 
# <center><img title="a title" alt="msc students" src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Master_students_pmf.png" width="700" 
#      height="200" /></center>

# In[4]:


display_quiz('quiz_2_1_3b.json')


# Determine whether each statement is TRUE or FALSE 

# In[5]:


display_quiz('quiz_2_1_3c.json')

