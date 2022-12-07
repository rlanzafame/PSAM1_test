#!/usr/bin/env python
# coding: utf-8

# # 1.1.6 Intersection (AND) and Union (OR)
# 
# 
# As previously introduced, we have a water supply system for a town with two water tower reservoirs, Tower A and Tower B. We can define the event that Tower A is full (event $A$) or empty ($\bar{A}$)). We can define the same events for Tower B (full, $B$), and empty, $\bar{B}$). Let’s represent them graphically.
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Sample_sapce_omega_int_uninon.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# As you can see, there is an overlap between $A$ and $B$, between $A$  and $\bar{B}$ and between $\bar{A}$ and $B$. Remember that there is no overlap between $A$  and $\bar{A}$ and between $B$ and $\bar{B}$because they are mutually exclusive (towers cannot be empty and full at the same time!).
# 
# The intersection of two events, $A$ and $B$, is constituted by the common points between the two events and it is denoted as $AB$ or  $A \cap B $. Thus, it is called the AND operator (the area where both $A$ and $B$ occur).
# 
# The overlap areas between $A$ and $B$, and between $\bar{A}$ and $\bar{B}$ are much wider. In other words, it is highly probable that if Tower A and Tower B are full or empty at the same time. This is important since we might think that we are building redundancy by having two towers, but if both are empty at the same time, it’s not as effective!
# 
# However, the capacity of one of the towers may be enough to supply the needed water. In that case, we would not be interested in both towers being full at the same time, but at least having one of them full. That is the union, which represents the joint or common occurrence of two events, and it is denoted as $A+B$ or $A \cup B $. Thus, it is called OR operator (the area where $A$ or $B$ occur). In the figure below, it is shown the graphical representation of $A \cap B $ and $A \cup B $.
# 
# Let’s consider whether or not an earthquake will occur during a one year period. Because there are only two possible outcomes (a binary event), $A$ and $\bar{A}$ are collectively exhaustive.
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/int_union.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="610" height="330" /></p>
# 
# ---
# 
# 
# # Solar panels
# 
# Let's test what you have learned about intersection and union!
# 
# Imagine we are planning to build a small solar panel facility to make more sustainable energy consumption in a domestic facility. Our solar panel facility is composed of 16 solar panels.
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Solar_panel.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# Once it is in operation, we will be able to reduce the amount of energy produced obtained from external sources. Consequently, we want to estimate the amount of time we will be able to cover the energy needs with our solar facility. 
# 
# Assuming that we need all 16 solar panels working at the same time to fulfil our energetic needs:
# 

# In[1]:


from jupyterquiz import display_quiz

display_quiz('quiz_1_1_6a.json')


# ---
# 
# # Water towers reservoirs
# 
# Let's go back to our previous example of the water tower reservoirs. Now, we will focus on the events that there is no water in the towers ($\bar{A}$ and $\bar{B}$).
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Not_a_not_b_res.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# ### Question 1
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/intersection_res.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>

# In[2]:


display_quiz('quiz_1_1_6b.json')


# ### Question 2
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/nor_in_not_un_res.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>

# In[3]:


display_quiz('quiz_1_1_6c.json')

