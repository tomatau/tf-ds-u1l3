#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

mean = 0
variance = 2
sigma = np.sqrt(variance) # this is the standard deviation
x = np.linspace(-5,5,50)
plt.plot(x, mlab.normpdf(x,mean,sigma))

print plt.show()