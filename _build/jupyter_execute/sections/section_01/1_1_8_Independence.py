#!/usr/bin/env python
# coding: utf-8

# # 1.1.8 Independence
# 
# Do you remember our example of the two reservoir towers? Tower A and Tower B were built to ensure the water supply system has sufficient capacity. We defined the event that Tower A is full (event $A$) or empty ($\bar{A}$), and similarly for Tower B (full, $B$ and empty, $\bar{B}$).
# 
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Sample_sapce_omega_int_uninon.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# 
# We want to make sure that there is enough water to meet the water demand in the town. That is why we installed two reservoirs, although most of the time if there is an average amount of rainfall, the system will have enough water with only one tower. It seems reasonable to assume that building two towers is good enough, right?
# 
# What we have not considered previously is the relationship between events $A$ and $B$. During a drought, it is more likely that both reservoirs are empty, whereas during a rainy year it is more likely that both reservoirs are full. In other words, a dependency exists between $A$ and $B$, since there are common drivers which influence whether or not the reservoirs are full or empty.
# 
# This is extremely important when assessing our system. If we do not consider this dependence, we may think that we are building a redundant system. However, since the amount of water in one tower is closely related to the other, we are not being effective and the system capacity may be on the unsafe side!
# In terms of probability, we see that if Tower A is empty, the probability that Tower B is empty is higher than what we might think if we didn't know about the condition of Tower A. The converse is also true. You will soon see that we can actually calculate this change in probability using our Venn diagrams and with the mathematics of probability, but first, we need a definition of independence.
# 
# > Two events are (stochastically or statistically) **independent** when the probability of occurrence of one of the events is not affected by the occurrence of another event. Conversely, if the probability of one event takes on a different value given the outcome of another event, they are dependent.
# 
# 
# 
