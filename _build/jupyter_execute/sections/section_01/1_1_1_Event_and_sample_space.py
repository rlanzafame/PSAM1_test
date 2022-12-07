#!/usr/bin/env python
# coding: utf-8

# # 1. Must-know probability concepts
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/must-know_probability_concepts.PNG" alt="" style="display: block; margin-left: auto; margin-right: auto;" width="400" height="230" /></p>
# 
# Welcome to the **Must-know probability concepts module**, which covers key concepts from probability theory needed to go further in your probability journey in CEG applications. This module is different than the others in this course since it lists many small concepts rather than focuses on one. This is because many of them should have been covered in a high school and bachelor-level course on statistics. Since there are many excellent textbooks and videos on the subject you should refer elsewhere if these concepts are completely unclear to you.
# 
# ---
# 
# ## Event and sample space
# 
# Sample space ($\Omega$) is the collection of all possible outcomes arising from an experiment or operation which involves chance. An event is the specific outcome, or set of outcomes, from the experiment or operation. Many natural disasters can be considered as binary events: either they occur or don't occur. This is analogous to flipping a coin, where the ‘flip’ is our experiment and heads or tails defines the two possible events. Our sample space is the set of two possible events.
# 
# For natural disasters, we often consider a specific time period, one year, as our experiment, with the sample space being our two possible events: occurrence or non-occurrence. We can refer to the disaster occurring as event $A$, and non-occurrence as event $A_c$. We communicate the probability of an event happening using a capital $P$, so the probability of $A$ occurring is $P(A)$.
# 
# Note:  $A_c$ is the complement of $A$ (sometimes called "not $A$"), and it follows from the axioms of probability that $P(A_c)=1-P(A)$. Sometimes other notation is used, for example, $\bar{A}$, which is read out as "$A$ bar".
# 
# This will be described in more detail below.
# 
# ---
# 
# Often it's useful to draw the events and sample space like this:
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/Sample_sapce_omega.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# 
# We can see our sample space is represented by the outline of the diagram, which also represents a probability of 1.0. The sample space has also been divided into two parts, and since the entire area is filled with $A$ and the complement of $A$ ($\bar{A}$), we know that these are the only two possible outcomes. Remember Venn diagrams from your high school statistics course? Often there was an overlap area between the two circles...but in the figure here that's not the case. Do you know why? We'll cover that in the next part of this module! But first, some simple questions about the sample space and events considered in the figure:
# 
# ### Quiz
# 
# This is notebook with a Jupyter Quiz in it. The Python cell is hidden from the site by using the `remove-input` cell tag.
# 

# In[1]:


from jupyterquiz import display_quiz

display_quiz('quiz_1_1_1.json')

