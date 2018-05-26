import sys
sys.path.append("..")

import numpy as np
import pylab as plt





fig=plt.figure(figsize=(22.62372, 6))  
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.30)
fig.subplots_adjust(top=.89)
fig.subplots_adjust(right=.52)
fig.subplots_adjust(left=.10)




sprite={1: 280, 2: 4, 3: 2, 4: 191, 5: 125}
##sd=1.73

ax.set_title('SD=1.73',fontsize=48)
ax.bar(range(1,6),sprite.values(),align='center',width=.75,color='k')
ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=30)
ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=30)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['bottom'].set_position(['outward',10])
ax.spines['left'].set_position(['outward',10])
##ax.spines['left'].set_bounds(0,100)
ax.spines['bottom'].set_bounds(1,5)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks(range(1,6))
ax.set_xticklabels(['1','2','3','4','5'])

ax.set_ylabel('Number',fontsize=48,labelpad=20)
ax.set_xlabel('Rating',fontsize=48,labelpad=20)
ax.set_xlim(.6,5.4)
plt.savefig('figure4b.pdf')
plt.savefig('figure4b.svg')
plt.show()


