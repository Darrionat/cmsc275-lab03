# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:10:39 2019

@author: Kerri Norton
"""

# Empirical Rule

import scipy.integrate
import random
import pylab


def gaussian(x, mu, sigma):
    """
    A function that represents a Gaussian curve.
    :param x: X-value to be computed.
    :param mu: The mean of the normal distribution.
    :param sigma: Standard deviation of curve.
    :return: The value of a normal curve with the given
            mean and standard deviation at the point x.
    """
    # The normal curve formula
    factor1 = (1.0 / (sigma * ((2 * pylab.pi) ** 0.5)))
    factor2 = pylab.e ** -(((x - mu) ** 2) / (2 * sigma ** 2))
    return factor1 * factor2


def checkEmpirical(numTrials):
    # Runs trials
    for t in range(numTrials):
        # A random mean between -10 and 10 (inclusive)
        mu = random.randint(-10, 10)
        # Random stdev
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        # The number of standard deviations to check
        for numStd in (1, 1.96, 2, 2.576):
            # Calculates the percentage of area underneath
            # mu plus/minus stdev
            area = scipy.integrate.quad(gaussian, mu - numStd * sigma,
                                        mu + numStd * sigma,
                                        (mu, sigma))[0]
            print('  Fraction within', numStd, 'std =',
                  round(area, 4))


checkEmpirical(2)
