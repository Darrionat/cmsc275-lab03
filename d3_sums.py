import random
import math
import pylab


def sim(num_trials):
    results = []
    sums = [0, 0, 0, 0, 0]
    for i in range(num_trials):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        s = x + y
        results.append(s)
        sums[s - 2] = sums[s - 2] + 1

    pylab.bar([2, 3, 4, 5, 6], sums)
    pylab.title('Sum of Two D3 Rolls (' + str(num_trials) + ' Trials)')
    pylab.xlabel('Value of Summed Rolls')
    pylab.ylabel('Frequency')


N = 6000
sim(N)
pylab.savefig('d3sums_' + str(N) + '_trials.pdf')
pylab.show()
