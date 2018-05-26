import sys
sys.path.append("..")

from pSPRITE import SPRITE
import numpy as np
import pylab as plt





fig=plt.figure(figsize=(22.62372, 6))  
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.26)
fig.subplots_adjust(top=.93)
fig.subplots_adjust(right=.99)
fig.subplots_adjust(left=.35)




x=SPRITE(19.4,1,19.9,1,45,0,51)
##make bins
data=[]
for low,high in zip([0]+range(1,52,5),[0]+range(5,57,5)):
    count=0
    print low,high
    for i in x[1]:
        if low<=i<=high:
            count+=x[1][i]
    data.append(count)

    

ax.bar(range(12),data,align='center',width=.75,color='k')
ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=24)
ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=24)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['bottom'].set_position(['outward',10])
ax.spines['left'].set_position(['outward',10])
##ax.spines['left'].set_bounds(0,100)
ax.spines['bottom'].set_bounds(0,11)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks(range(12))
ax.set_xticklabels(['0']+[str(i)+'-'+str(j) for i,j in zip(range(1,47,5),range(5,51,5))]+['51'])



ax.set_ylabel('Number',fontsize=48,labelpad=10)
ax.set_xlabel('Carrots Taken',fontsize=48,labelpad=10)
ax.set_xlim(-.5,11.5)
##ax.set_ylim(0,float(ylabels[-1].get_text())/1000+.0005)
plt.savefig('figure3b.pdf')
plt.savefig('figure3b.svg')
plt.show()


