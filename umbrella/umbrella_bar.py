from itertools import *
import pylab as plt


data=(1, 1, 1, 1, 1, 1, 1, 1, 5, 5)

counts={}
for i in data:
    counts[i]=counts.get(i,0)+1

fig=plt.figure(figsize=(22.62372, 12))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.08)
fig.subplots_adjust(left=.05)
fig.subplots_adjust(right=1.0)
fig.subplots_adjust(top=.95)
ax.bar(counts.keys(),counts.values(),color='k',align='center',width=.75)
ax.tick_params(axis='x',length=0,width=2,direction='out',labelsize=80,pad=5)
ax.tick_params(axis='y',length=15,width=0,direction='out',labelsize=80,pad=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_position(['outward',0])
ax.spines['left'].set_position(['outward',-5])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
##ax.set_xlabel('Means',fontsize=30)
##ax.set_ylabel('Standard Deviations',fontsize=30)
##ax.set_title('Sample Size=10',fontsize=40)
ax.set_xlim(0.5,5.5)
##ax.set_yticks(range(0,18,2))
##ax.set_ylim(-.02,2.3)
plt.savefig('bar.svg')
plt.savefig('bar.pdf')
plt.show()




