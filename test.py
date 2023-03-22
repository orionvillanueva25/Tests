# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:56:48 2023

@author: orion
"""

#vamos diretos aos posteriors

import numpy as np
from scipy.stats import poisson
from scipy.stats import gamma
import scipy.special as sps  
import matplotlib.pyplot as plt
import math
'''
def uniform_change(data):
    r = np.sum(data) + 1
    v = len(data)
    return r, v

def jeff_change(data):
    r = np.sum(data) + 0.5
    v = len(data)
    return r, v
'''
def gamma_change(data, shape, scale):
    r = np.sum(data) + shape
    v = len(data) + scale
    return r, v

#constants
mu = 2
events = 1000

#sampler
data = poisson.rvs(mu, size = events)   

''' 
uniform prior uses shape = 1 and scale = 0
jeff prior uses shape = 0.5 and scale = 0
'''
r, v = gamma_change(data, shape = 1 , scale = 2)

    
#posterior 
shape, scale = r, v  
posterior = np.random.gamma(shape, scale, events)

#stats
mean = r/v
var = r/(v**2)

#graphic
count, bins, ignored = plt.hist(posterior, 30, density=True)
y = (bins**(shape-1))*(np.exp(-bins/scale) /  
                     (sps.gamma(shape)*scale**shape))
print(y)

plt.plot(bins, y, linewidth=2, color='r')
plt.show() 
    
print(f"mean= {mean} and variance = {var}")
