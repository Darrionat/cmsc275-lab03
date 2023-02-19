import random
import math
import pylab


def sim(num_trials):
    results = []
    sums = [0, 0, 0]
    for i in range(num_trials):
        x = random.randint(1, 3)
        results.append(x)
        sums[x - 1] = sums[x - 1] + 1

    pylab.bar([1, 2, 3], sums)
    pylab.title('D3 Rolls (' + str(num_trials) + ' Trials)')
    pylab.xlabel('Value of Roll')
    pylab.ylabel('Frequency')


N = 3000
sim(N)
pylab.savefig('d3_' + str(N) + '_trials.pdf')
pylab.show()
