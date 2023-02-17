# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:57:35 2019

@author: Kerri Norton
"""

import random
import pylab


def flip(numFlips):
    """
    Flips a coin a given number of times and then returns the proportion of heads flipped.
    :param numFlips: The total number of flips to do. Assumed to be a positive integer.
    :return: Returns the proportion of heads flipped.
    """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / numFlips


extreme_lower = .25
extreme_upper = .75


def regressToMean(numFlips, numTrials):
    """
    Creates a plot based upon a given number of flips for multiple trials.
    :param numFlips: The number of each flips during each trial.
    :param numTrials: The number of trials
    """
    # Get fraction of heads for each trial of numFlips
    fracHeads = []
    # Run trials
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    # Find trials with extreme results and for each the next trial
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        # Extremes are outside the interval [.33, .66]
        if fracHeads[i] < extreme_lower or fracHeads[i] > extreme_upper:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i + 1])

    # Plot results
    pylab.plot(range(len(extremes)), extremes, 'ko',
               label='Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^',
               label='Next Trial')

    # Adds horizontal line at y = 0.5
    pylab.axhline(0.5)
    # Limit plot view
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)

    # Set up the chart
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc='best')


regressToMean(15, 500)
pylab.savefig('regress_15_500_more_extremes.pdf')
pylab.show()
