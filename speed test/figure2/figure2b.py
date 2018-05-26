import os
import pylab as plt
import numpy as np
import math
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

f=open(os.path.join(BASE_DIR,'corvids_v1_times1.txt'))
run_1=[[int(i.split()[0]),float(i.split()[1])] for i in f]


f=open(os.path.join(BASE_DIR,'corvids_v1_times2.txt'))
run_2=[[int(i.split()[0]),float(i.split()[1])] for i in f]


f=open(os.path.join(BASE_DIR,'corvids_v1_times3.txt'))
run_3=[[int(i.split()[0]),float(i.split()[1])] for i in f]


##plot the data with pylab
fig=plt.figure(figsize=(22.62372, 6))  
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.20)
fig.subplots_adjust(top=.98)
fig.subplots_adjust(right=.99)
fig.subplots_adjust(left=.07)

ax.plot([i[0] for i in run_1],[i[1] for i in run_1],linewidth=2.0,color="#f4b541")
ax.plot([i[0] for i in run_2],[i[1] for i in run_2],linewidth=2.0,color="#f4b541")
ax.plot([i[0] for i in run_3],[i[1] for i in run_3],linewidth=2.0,color="#f4b541")


f=open(os.path.join(BASE_DIR,'corvids_v2_times1.txt'))
run_1=[[int(i.split()[0]),float(i.split()[1])] for i in f]


f=open(os.path.join(BASE_DIR,'corvids_v2_times2.txt'))
run_2=[[int(i.split()[0]),float(i.split()[1])] for i in f]


f=open(os.path.join(BASE_DIR,'corvids_v2_times3.txt'))
run_3=[[int(i.split()[0]),float(i.split()[1])] for i in f]


ax.plot([i[0] for i in run_1],[i[1] for i in run_1],linewidth=2.0,color="#d37f02")
ax.plot([i[0] for i in run_2],[i[1] for i in run_2],linewidth=2.0,color="#d37f02")
ax.plot([i[0] for i in run_3],[i[1] for i in run_3],linewidth=2.0,color="#d37f02")



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
ax.set_ylabel('Time (s)',fontsize=48,labelpad=20)
ax.set_xlabel('Sample Size',fontsize=48,labelpad=20)
ax.set_xlim(2,99)
ax.set_ylim(0,805)
plt.savefig('figure2b.svg')
plt.savefig('figure2b.pdf')
plt.show()
