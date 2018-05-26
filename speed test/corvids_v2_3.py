import sys
sys.path.append("../corvids_v2")

from RecreateData import *
import numpy as np
import pylab as plt
import time


decimals=2
def std(data,u):
    return (sum([(i-u)**2 for i in data])/(len(data)-1))**.5

f=open('corvids_v2_times3.txt','w')
f.close()
for n in range(2,100):
    print n
    for i in range(1):
        i=np.random.choice(range(1,8),n)
        u=round(sum(i)/float(len(i)),decimals)
        var=round(np.var(i,ddof=1),decimals)
        rd = RecreateData(min_score=1, max_score=7, num_samples=n, mean=u, variance=var,\
                          mean_precision=.5/float(10**decimals),variance_precision=.5/float(10**decimals),\
                          debug=False)
        start=time.clock()
        rd.recreateData(multiprocess=False,find_first=False)
        end=time.clock()
        print end-start, len(rd.sols.values()[0])
        f=open('corvids_v2_times3.txt','a')
        f.write(str(n))
        f.write('\t')
        f.write(str(end-start))
        f.write('\t')
        f.write(str(len(rd.sols.values()[0])))
        f.write('\n')
    print
f.close()



