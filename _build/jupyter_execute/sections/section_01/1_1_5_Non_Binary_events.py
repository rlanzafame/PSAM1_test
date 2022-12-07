#!/usr/bin/env python
# coding: utf-8

# # 1.1.5 Non Binary events
# 
# Note that we chose to define the natural disaster as binary, but this is not always useful. Sometimes we are interested in the number of events per year, or perhaps a discrete or continuous representation of the event, for example, earthquake magnitude as a continuous random variable, or severity of droughts as a discrete variable (e.g., the intensity measured as mild, moderate or severe). We will consider these cases in other modules of the course.
# 
# 
# Let’s explore this more with a new example!
# 
# ---
# 
# 
# 
# <p><img src="https://raw.githubusercontent.com/mike-mendoza/-PSAM1_test/main/images/water_tower.png
# " alt="" style="display: block; margin-left: auto; margin-right: auto;" width="310" height="330" /></p>
# 
# 
# Imagine a water supply system for a town that has two water tower reservoirs, Tower A and Tower B. We want to make sure that there is enough water in the reservoirs to supply the town with fresh water. In a broader sense, we know that these towers are part of a larger water distribution network, so we are really interested in the chance that the towers can provide sufficient water or not, since this information can be used to design and build the rest of the water system in a reliable and resilient way. So, with that in mind, there are several ways we can define the volume of water stored in a reservoir:
# 
#     a). Either full or empty
#     b). Partially filled, measured as empty, ¼, ½, ¾, full.
#     c). Partially filled, measured as a number from 0 to the maximum volume v.
# 
# 
# Option a would define the volume of water as a) binary variable since only two options would be possible. Option b) would define it as a discrete variable since the volume would be defined in a countable subset of the real numbers. Finally, option c) would model volume as a continuous variable, since it would define the variable in an uncountable subset of the real numbers. 
# 
# We will see more examples of non-binary events later. For now, we will focus on binary and discrete cases (cases a) and b)).
# 
