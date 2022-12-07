#!/usr/bin/env python
# coding: utf-8

# # 1.1.7 Axioms
# 
# Let's talk quickly about axioms
# 
# As you may remember from a previous course on probability and statistics, there are some basic statements that always hold when talking about probability. They are called axioms! You can easily find out more details with a quick internet search, so let's quickly review a few key points.
# 
# The first two axioms tell us that probabilities can take values from 0 to 1, with the probability of the whole sample space equal to 1.
# 
# $ 0 \leq P(A) \leq 1$
# 
# $P(\Omega) =  1$
# 
# Based on the previous discussion in this module we can see that if two events are mutually exclusive, the following holds:
# 
# $P(A \cup B)  = P(A) + P(B) $
# 
# This is the third axiom of probability! Remember that two events being mutually exclusive means that the occurrence of one event excludes the other, so they do not have points in common in the Venn diagrams. However, if they do have points in common, we need to subtract that area. Mathematically, that looks like this:
# 
# $P(A \cup B)  = P(A) + P(B) - P(A \cap B)$
# 
# The axioms of probability may seem simple, but they are incredibly powerful because they support a number of mathematical rules as well as allowing us to represent all sorts of physical phenomenon, which we will see throughout this course and those that follow. One quick example is how we can combine the second and third axioms of probability to prove that if two events are collectively exhaustive their union represents the entire sample space and the probability of the union is therefore 1.0. In our earthquake example, this means that the probability of the earthquake happening or not happening is 1.0.
