# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:51:52 2019

@author: Kerri Norton
"""
import random
import pylab
import math

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


def roll(numRolls):
    """Assumes numFlips a positive int"""
    ones = 0
    for i in range(numRolls):
        if random.randint(1, 3) == 1:
            ones += 1
    return ones / float(numRolls)


def rollSim(numRollsPerTrial, numTrials):
    fracOnes = []
    for i in range(numTrials):
        fracOnes.append(roll(numRollsPerTrial))
    mean = sum(fracOnes) / len(fracOnes)
    sd = stdDev(fracOnes)
    return fracOnes, mean, sd


def labelPlot(numRolls, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of '
                + str(numRolls) + ' rolls each')
    pylab.xlabel('Fraction of Ones')
    pylab.ylabel('Number of Trials')
    pylab.annotate('Mean = ' + str(round(mean, 4)) \
                   + '\nSD = ' + str(round(sd, 4)), size='x-large',
                   xycoords='axes fraction', xy=(0.67, 0.5))


def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = rollSim(numFlips1, numTrials)
    pylab.hist(val1, bins=20)
    xmin, xmax = pylab.xlim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = rollSim(numFlips2, numTrials)
    pylab.hist(val2, bins=20)
    pylab.xlim(xmin, xmax)
    labelPlot(numFlips2, numTrials, mean2, sd2)


# Figure 15.24
def showErrorBars(minExp, maxExp, numTrials):
    """Assumes minExp and maxExp positive ints; minExp < maxExp
         numTrials a positive integer
       Plots mean fraction of heads with error bars"""
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2 ** exp)
        frac_ones, mean, sd = rollSim(2 ** exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, means, yerr=1.96 * pylab.array(sds), ecolor='red')
    pylab.semilogx()
    pylab.title('Mean Fraction of Ones ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of rolls per trial')
    pylab.ylabel('Fraction of ones & 95% confidence')


min_exp = 3
max_exp = 15
numTrials = 2000
showErrorBars(min_exp, max_exp, numTrials)
pylab.savefig('meanFracOnes_' + str(min_exp) + 'to' + str(max_exp) + '_' + str(numTrials) + 'trials.pdf')
pylab.show()
