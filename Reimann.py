# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:29:40 2020

@author: islam
"""
import numpy as np

# Defining Functions #
def function(var):
    #Try to declare the domain of the funtion, such as 'if var <= 0: return 0' for ln function etc.
    
    #Try to give var as your independent variable, function should be explicid
    return np.cos(var)
    
# Reimann summ method

def reimann(nFrom, nTo):
    # This is get more accurate as you chose larger the step, but I think 10x10^4 is enough
    step = 100000
    result = 0
    for x in range((nTo-nFrom)*step):
        result = result + function(x/step)/step
    return round(result,3)

#int cosx 0 to 1
print(reimann(0,1))
