
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
print(stats.describe(a))

b = np.random.normal(0, 2, size=pts)
#x = np.concatenate((a, b))
#k2, p = stats.normaltest(a)
result = stats.ttest_1samp(a,0.041)

x=range(0,1000)

#fig=plt.figure(figsize=(8.0,7.5))
#plt.scatter(x,a)
#plt.savefig('han.png')

print(result.statistic)
print(result.pvalue)

p=result.pvalue
alpha = 1e-3
print("p = {:g}".format(p))

if p < alpha:  # null hypothesis: x comes from a normal distribution
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")
