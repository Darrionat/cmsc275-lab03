# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:51:52 2019

@author: Kerri Norton
"""
import random
import math
import pylab

vals = []


def sum_squared_deviations_computational(samples):
    """
    Computes the sum of squared deviations from the mean of the given list using the computational formula.
    :param samples: A non-empty list of numerical values.
    :return: Returns the sum of squared deviations from the mean.
    """
    # The sum of all points after being squared
    sum_x_squared = 0
    # The sum of all points
    sum_x = 0
    for x in samples:
        sum_x_squared += pow(x, 2)
        sum_x += x
    # The computational formula
    return sum_x_squared - pow(sum_x, 2) / len(samples)


def variance(X, population=True):
    SS = sum_squared_deviations_computational(X)
    N = len(X)
    # Population variance
    if population:
        return SS / N
    # Avoid size 1 samples
    if N == 1:
        raise ArithmeticError('Cannot have sample of length 1')
    return SS / (N - 1)


def stdDev(X, population=True):
    if population:
        return math.sqrt(variance(X))
    return math.sqrt(variance(X, False))


def flip(numFlips):
    """Assumes numFlips a positive int"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / float(numFlips)


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)


def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of '
                + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    pylab.annotate('Mean = ' + str(round(mean, 4)) \
                   + '\nSD = ' + str(round(sd, 4)), size='x-large',
                   xycoords='axes fraction', xy=(0.67, 0.5))


def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)


makePlots(10, 1000, 100)
pylab.show()

# vals = [0,1,3,3,2,2,1,0,1,5,4,4,3]
# print(variance(vals))
# vals2 = [2,2,1,0,2,1]
# print(variance(vals2))
