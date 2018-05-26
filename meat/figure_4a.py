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




##convert dict back to list
#sd=1.25
sprite={1: 119, 2: 167, 3: 6, 4: 310}
    
ax.set_title('SD=1.25',fontsize=48)
ax.bar(range(1,6),sprite.values()+[0],align='center',width=.75,color='k')
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
plt.savefig('figure4a.pdf')
plt.savefig('figure4a.svg')
plt.show()


