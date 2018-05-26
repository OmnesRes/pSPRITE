from itertools import *
import pylab as plt



#my own variance function runs much faster than numpy or the Python 3 ported statistics module
def variance(data,u):
    return sum([(i-u)**2 for i in data])/len(data)


##rounding the means and variances helps to collapse them
precision_ave=16
precision_var=12
n=8
r=10
all_deviations={}
for i in combinations_with_replacement(range(-1,n), r):
    u=round(sum(i)/float(len(i)),precision_ave)
    var=round(variance(i,u),precision_var)
    if var not in all_deviations:
        all_deviations[var]={u:[i]}
    else:
        if u in all_deviations[var].keys():
            all_deviations[var][u]=all_deviations[var][u]+[i]
        else:
            all_deviations[var][u]=[i]

sds=[]
means=[]

for i in all_deviations.keys():
    sds+=[(i*r/(r-1))**.5]*len(all_deviations[i].keys())
    means+=list(all_deviations[i].keys())

new_means=[]
new_sds=[]
for i,j in zip(means,sds):
    if 1.0<=i<=5.0:
        new_means.append(i)
        new_sds.append(j)


fig=plt.figure(figsize=(22.62372, 12))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=.10)
fig.subplots_adjust(left=.07)
fig.subplots_adjust(right=1.0)
fig.subplots_adjust(top=.99)
ax.scatter(new_means,new_sds,color='k',s=80)
ax.vlines(2.05,-0.01,2.3,color='r',linewidth=25,alpha=.5)
ax.vlines(3.0,-0.01,2.3,color='#ff9966',linewidth=5,zorder=-5)
ax.tick_params(axis='x',length=0,width=2,direction='out',labelsize=30)
ax.tick_params(axis='y',length=15,width=0,direction='out',labelsize=30,pad=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_linewidth(3)
ax.spines['bottom'].set_position(['outward',0])
ax.spines['left'].set_position(['outward',-5])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlabel('Means',fontsize=48)
ax.set_ylabel('Standard Deviations',fontsize=48)
##ax.set_title('Sample Size=10',fontsize=40)
ax.set_xlim(.98,5.02)
##ax.set_yticks(range(0,18,2))
ax.set_ylim(-.02,2.3)
plt.savefig('figure1a.svg')
plt.show()




