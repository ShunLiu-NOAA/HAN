
from scipy import stats
import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset

pts = 1000
np.random.seed(28041990)
a = np.random.normal(0, 1, size=pts)
b = np.random.normal(2, 1, size=pts)
x = np.concatenate((a, b))
plt.plot(a)
k2, p = stats.normaltest(x)
print(k2)
alpha = 1e-3
print("p = {:g}".format(p))

if p < alpha:  # null hypothesis: x comes from a normal distribution
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")
