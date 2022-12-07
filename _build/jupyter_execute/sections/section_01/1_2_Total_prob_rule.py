#!/usr/bin/env python
# coding: utf-8

# ## Total Probability Rule
# ### Tulip fields
# ---
# 
# The fields of tulips located in a coastal area receive water from both ground water (an aquifer) and surface water (a river with a storage device). The operation of this supply system is influenced by the regional droughts which occur randomly with an annual frequency of 15%. There is a 60% chance that extremely low flows will occur in the river during a regional drought. During a year with extremely low flows due to a regional drought, there is a 40% chance to have a failure in the system due to the lack of water in either of the sources. Also, there is a 20% chance that the aquifer is polluted due to brackish water in a year with extremely low flows and there is a 10% chance to have a failure in the system during a dry year when low flows do not occur due to the lack of stored water. 
# 
# The goal is to determine the probability of having a failure in the water supply of the fields of tulips, P(failure).
# 
# ---
# 

# 1. What is the probability of having a drought and low flows?

# In[1]:


p_drought = 0.15 #Probability of having a drought
p_low_given_drought = 0.60 #Probability of having low flows during a regional drought
p_shortage_surface_given_low_AND_drought = 0.4 #Probability of having a shortage during a dry year with low flows caused by any of the two sources.
p_failure_given_shortage_surfaceC_AND_low_AND_drought = 0.2 #Probability of having a shortage during a dry year with low flows which do not cause directly a shortage.

p_low_AND_drought = p_low_drought * p_drought

print(f'The probability is {p_low_AND_drought:.3f}')


# 2. What is the probability of having a drought but not having low flows?

# In[5]:


p_drought = 0.15 #Probability of having a drought
p_low_given_drought = 0.60 #Probability of having low flows during a regional drought
p_shortage_surface_given_low_AND_drought = 0.4 #Probability of having a shortage during a dry year with low flows caused by any of the two sources.
p_failure_given_shortage_surfaceC_AND_low_AND_drought = 0.2 #Probability of having a shortage during a dry year with low flows which do not cause directly a shortage.


p_lowC_AND_drought = (1-p_low_given_drought) * p_drought

print(f'The probability is {p_lowC_AND_drought:.3f}')


# 3. We can assume that low flows in the river occur only when there is a drought, so $P(\mathrm{drought}^c \cap \mathrm{low}) = 0 $ and $P(\mathrm{low}^c|\mathrm{drought}^c) = 1 $. Then, which is the probability of not having low flows in a year and not having a regional drought?

# In[6]:


p_drought = 0.15 #Probability of having a drought

p_lowC_AND_droughtC = 1*(1-p_drought)

print(f'The probability is {p_lowC_AND_droughtC:.3f}')


# In[ ]:




