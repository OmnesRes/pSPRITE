import sys
sys.path.append("..\..")

from pSPRITE import SPRITE
import numpy as np
import pylab as plt
import time


decimals=2
def std(data,u):
    return (sum([(i-u)**2 for i in data])/(len(data)-1))**.5


failed=[]


fig=plt.figure(figsize=(22.62372, 6))  
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.20)
fig.subplots_adjust(top=.99)
fig.subplots_adjust(right=.99)
fig.subplots_adjust(left=.07)



for run in range(3):
    print run
    times=[]
    for n in range(2,100):
        i=np.random.choice(range(1,8),n)
        u=round(sum(i)/float(len(i)),decimals)
        sd=round(std(i,u),decimals)
        start=time.clock()
        x=SPRITE(u,decimals,sd,decimals,n,1,7)
        end=time.clock()
        if type(x)==type('string'):
            failed.append(x)
        times.append(end-start)
    plt.plot(range(2,100),times,linewidth=2.0,color="#4286f4",label="pSPRITE")



ax.tick_params(axis='y',length=0,width=0,direction='out',labelsize=16)
ax.tick_params(axis='x',length=0,labelsize=16,pad=5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_position(['outward',0])
ax.yaxis.set_ticks_position('left')
ax.set_xticks([i for i in range(2,100)])
ax.set_xticklabels([str(i) for i in range(2,100)],rotation=270)
fig.canvas.draw()
ylabels=ax.get_yticklabels()
ax.set_yticklabels([str(int(float(i.get_text())*1000)) for i in ylabels])
ax.set_ylabel('Time (ms)',fontsize=48,labelpad=20)
ax.set_xlabel('Sample Size',fontsize=48,labelpad=20)
ax.set_xlim(2,99)
ax.set_ylim(0,float(ylabels[-1].get_text())/1000+.0005)
plt.savefig('figure2a.pdf')
plt.savefig('figure2a.svg')
plt.show()


plt.show()

