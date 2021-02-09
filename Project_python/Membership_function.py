import numpy as np 
from matplotlib import pyplot as plt
from plot_memb_funct import *

def trapmf(x, parameter):
    """
    Parameters
    ----------
    Fnction: trapmf(x, [a, b, c, d]): trapezoidal membership function
    x : Integer, float or numpy.ndarray 
        DESCRIPTION. Contain x values in the universe to evaluate
        in membership function.
    parameter: [a, b, c, d] list, numpy.ndarray.
        DESCRIPTION. Contain parameters of memberhip function,
        should fulfill: a <= b <= c <=d 
    Returns
    -------
    Membership value of x according the trapezoidal membership
        DESCRIPTION.
        trapmf(x, param): float, if x es int, float.
        trapmf(x, param): numpy.ndarray: if x es numpy.ndarray

    """
    a = float(parameter[0])
    b = float(parameter[1])
    c = float(parameter[2])
    d = float(parameter[3])
    if (a <= b) and (b <= c) and (c <= d):
           
        y = np.zeros(x.size)
        for i in range(x.size):
            if x[i] < a:
                y[i] = 0.0
            elif (a <= x[i]) and (x[i] < b):
                y[i] = (x[i] - a)/(b - a)   
            elif (b <= x[i]) and (x[i] <= c):
                y[i] = 1.0
            elif (c < x[i]) and (x[i] <= d):
                y[i] = (d - x[i])/(d - c)  
            else:
                y[i] = 0.0
        return y
    else:
        return -1


# Generate universe variables
#   * Quality and service on subjective ranges [0, 10]
#   * Tip has a range of [0, 25] in units of percentage points
depth = np.linspace(0, 1.45, 1500)
velocity = np.linspace(0, 3.4, 1500)
HSI  = np.linspace(0, 1, 1500)

# Generate fuzzy membership functions
depth_low = trapmf(depth, [0, 0, 0.15, 0.35])
depth_medium = trapmf(depth, [0.15, 0.35, 0.8, 1.1])
depth_high = trapmf(depth, [0.8, 1.1, 1.45, 1.45])

vel_low = trapmf(velocity, [0, 0, 0.4, 1])
vel_medium = trapmf(velocity, [0.4, 1, 1.4, 2])
vel_high = trapmf(velocity, [1.4, 2, 3.4, 3.4])

HSI_low = trapmf(HSI, [0, 0, 0.1, 0.3])
HSI_medium = trapmf(HSI, [0.1, 0.3, 0.7, 0.9])
HSI_high = trapmf(HSI, [0.7, 0.9, 1, 1]) 





        
