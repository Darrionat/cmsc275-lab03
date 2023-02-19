import scipy
from scipy.stats import norm
import numpy as np
import pylab

mean = 1
stdev = 3
x = 0.5
print(round(norm.ppf(x, mean, stdev), 4))

x_min = mean - 3.5 * stdev
x_max = mean + 3.5 * stdev
x_values = np.linspace(x_min, x_max, 10000)
pylab.title('Probability Point Function')
pylab.xlabel('Value')
pylab.ylabel('Probability Point')
pylab.plot(x_values, norm.ppf(x_values, mean, stdev))
pylab.savefig('distPPF' + str(mean) + '_' + str(stdev) + '.pdf')
pylab.show()
