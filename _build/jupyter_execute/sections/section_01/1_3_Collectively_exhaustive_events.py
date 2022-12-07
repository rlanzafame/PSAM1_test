#!/usr/bin/env python
# coding: utf-8

# # 1.3 Collectively exhaustive events
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Sample_sapce_omega.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# Two events are collectively exhaustive if at least one of them occurs whenever the experiment is performed. This can be illustrated by the previous set of figures, where the one with $A$ and $\bar{A}$ are collectively exhaustive because they fill up the entire sample space. In contrast, the figure with events $A$ and $B$ left a blank, unlabeled area in the sample space (the probability that nothing happens). This may seem simple and obvious now, but it has important implications when making probability calculations, which you will see in other modules (for example, the total probability rule). In addition, the union of collectively exhaustive events constitutes the sample space of that experiment. We will see the formal concept of union a bit later. For now, just know that the union is represented by the total area covered by our set of events, in this case, $A$ and $\bar{A}$, and that the probability of the union is equal to 1.0
# 
# ---
# 
# Let’s consider whether or not an earthquake will occur during a one year period. Because there are only two possible outcomes (a binary event), $A$ and $\bar{A}$ are collectively exhaustive.
# 
# # 1.3 Quiz
# 
# This is notebook with a Jupyter Quiz in it. The Python cell is hidden from the site by using the `remove-input` cell tag.
# 

# In[1]:


from jupyterquiz import display_quiz

display_quiz('quiz_1_3.json')

