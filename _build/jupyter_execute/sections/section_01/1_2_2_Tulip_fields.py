#!/usr/bin/env python
# coding: utf-8

# # 1.2.2 Tulip fields
# 
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/tulip_field.jpg
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="210" height="130" /></p>
# 
# Tulip fields are one of the major touristic attractions in an area in South Holland, as well as an important source of income. Thus, the Public Authority in the area wants to know how vulnerable those fields are. Would you help them calculate the probability of the tulips being damaged in a given year, $ P(A)$? Fortunately, you have already been provided historic data from which you can derive probabilities of bad events happening, $P(B_i)$, as well as the probability that such an event leads to damage, $P(A|B_i)$, which are summarized below.  
# 
# First, there may be a regional drought with a probability $ P(B_1)=0.05$ or a pipe in the supply system may break with a probability $P(B_2)=0.10$. There is a chance of $P(A|B_1)=0.65$ and $P(A|B_2)=0.55$ that tulips won’t grow if the regional drought or the pipe breakage happens, respectively. 
# 
# There may also be a human error in the operation of the water supply system, $P(B_3)=0.03$, which may make tulips be too dry or too wet and results in rotten tulips with a probability $P(A|B_3)=0.90$.
# 
# Another possibility is that the stored water to ensure the supply may get polluted, $P(B_4)=0.05$, leading to a lack of water for the tulips with chance $P(A|B_4)=0.70$.
# 
# Also, catastrophes can happen! There may be a plague or a fire that occurs with probabilities $P(B_5)=0.03$ and $P(B_6)=0.05$, respectively. Those can lead to damage in the tulips field with probabilities $P(A|B_5)=0.80$ and $P(A|B_6)=0.90$.
# 
# Find a summary below.
# 
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Tulip_T1.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="300" height="170" /></p>
# 
# ---
# 
# **1. Assuming that the described events are independent, mutually exclusive, and collectively exhaustive, apply the Total Probability Theorem to calculate the probability of tulips being damaged one year, P(A).**
# 
# You can write out the total probability rule by hand, but often it is useful to keep track of all the individual events in a table:
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Tulip_T2.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="330" height="170" /></p>
# 
# Therefore the probability of tulips being damaged one year is **0.219**
# 
# ---
# 
# **2. Considering the values in the table bellow, which of the following actions should the Public Authority take first?**
# 
#     a). Improve the maintenance of the pipes in the supply system
#     b). Further automate the operation to prevent human errors
#     c). Improve safety protocols to prevent fire 
#     
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Tulip_T3.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="350" height="130" /></p>
# 
# By looking at the values in the table we can say that the answer is "a) Improve the maintenance of the pipes in the supply system."
# 
# This is because the cause which contributes the most to the damages in the fields is the pipe breakage in the supply system. Thus, **improving their maintenance** may be one way to reduce $P(B_2)$. We could also try to reduce the value of  $P(A|B_2)$. Since this value is conditional on broken pipes, it obviously is a function of what happens at the tulip farm after the pipe breaks, for example, a leaky pipe detection system, or a backup water delivery system. If we can address those parts of the entire tulip growing system we can effectively reduce the overall probability of tulip damage.

# In[ ]:




