#!/usr/bin/env python
# coding: utf-8

# # 1.2.3 Concrete compressive strength
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Concrete_cores_tot_prob.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="210" height="130" /></p>
# 
# The Table 1 shows the concrete compressive strength of 60 concrete core samples ($ f_{c}^{'}$, in $ \mathrm{MPa} $) taken in different buildings. The sample space can be represented by the foregoing mutually exclusive, collectively exhaustive events $ \mathrm{B1}  $, $ \mathrm{B2}  $, $ \mathrm{B3}  $, and $ \mathrm{B4} $, where:
# 
# $ \mathrm{B1} \equiv \left \{11.57 \leq f_{c}^{'} < 18.78 \, \mathrm{MPa} \right \}$
# 
# $ \mathrm{B2} \equiv \left \{18.78 \leq f_{c}^{'} < 26.00 \, \mathrm{MPa} \right \}$
# 
# $ \mathrm{B3} \equiv \left \{26.00 \leq f_{c}^{'} < 33.21 \, \mathrm{MPa} \right \}$
# 
# $ \mathrm{B4} \equiv \left \{ f_{c}^{'} \geq  33.21 \, \mathrm{MPa} \right \}$
# 
# Suppose an engineer is interested in estimating the probability that the concrete compressive strength ranges from 20 to 30  $\mathrm{MPa} $, that is, the event:
# 
# $ \mathrm{A} \equiv \left \{20 \leq f_{c}^{'} < 30\, \mathrm{MPa} \right \}$
# 
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Sample_sapce_concret_tot_prob.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;"  width="330" height="170" /></p>
# 
# Table 1. Ranked concrete compressive strength data for concrete core samples in $\mathrm{MPa}$, in ascending order
# 
# The frequency distribution is given in the following table:
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Frequency_table_tot_prob.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="170" /></p>
# 
# Please answer the following questions:
# 
# # 1.2.3 Quiz
# 
# This is notebook with a Jupyter Quiz in it. The Python cell is hidden from the site by using the `remove-input` cell tag.
# 

# In[1]:


from jupyterquiz import display_quiz

display_quiz('quiz_1_2_3.json')

