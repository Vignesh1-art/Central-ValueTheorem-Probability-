import numpy.random as rn
import numpy as np
import matplotlib.pyplot as h
mean_of_samples=[]
no_of_samples=1000
for i in range(no_of_samples):
    sample=rn.randint(0,10,10)
    mean_of_samples.append(np.mean(sample))
h.hist(mean_of_samples)
h.show()
