import numpy.random as rn
import numpy as np
import matplotlib.pyplot as h
a=[]
for i in range(500):
    sample=rn.randint(0,10,10)
    a.append(np.mean(sample))
h.hist(a)
h.show()
