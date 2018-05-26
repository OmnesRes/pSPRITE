import sys
sys.path.append("..")

from pSPRITE import SPRITE
import numpy as np
import pylab as plt

##restrictions=[16,16]
##for i in range(10):
##    print SPRITE(9.8,1,9.2,1,31,0,15,restrictions=restrictions)
#closest:
sprite={0: 10, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 18, 16: 2}
##sd=7.306205934771502

fig=plt.figure(figsize=(22.62372, 6))  
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.30)
fig.subplots_adjust(top=.89)
fig.subplots_adjust(right=.99)
fig.subplots_adjust(left=.10)
ax.set_title('n=2 at 16oz, SD=7.31',fontsize=48)
ax.bar(sprite.keys(),sprite.values(),align='center',width=.75,color='k')
ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=30)
ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=30)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_linewidth(3)
ax.spines['bottom'].set_position(['outward',10])
ax.spines['left'].set_position(['outward',10])
##ax.spines['left'].set_bounds(0,100)
ax.spines['bottom'].set_bounds(0,max(sprite.keys()))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks([i for i in sprite.keys() if i%2==0])
##ax.set_xticklabels(['1','2','3','4','5'])

ax.set_ylabel('Number',fontsize=48,labelpad=20)
ax.set_xlabel('Estimated oz',fontsize=48,labelpad=20)
ax.set_xlim(-.4,max(sprite.keys())+.4)
plt.savefig('figure5a.pdf')
plt.savefig('figure5a.svg')
plt.show()


