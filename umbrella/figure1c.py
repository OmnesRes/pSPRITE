from itertools import *
import pylab as plt
import numpy as np
import math
def std(data,u):
    return (sum([(i-u)**2 for i in data])/(len(data)-1))**.5


##rounding the means and variances helps to collapse them
precision_ave=12
precision_var=10

def run(n,r):
    all_deviations={}
    for loop in range(1000000):
        i=np.random.choice(range(1,6),10)
        u=round(sum(i)/float(len(i)),precision_ave)
        var=round(std(i,u),precision_var)
        if var not in all_deviations:
##            all_deviations[var]={u:[i]}
            all_deviations[var]={u:1}
        else:
            if u in all_deviations[var].keys():
##                all_deviations[var][u]=all_deviations[var][u]+[i]
                all_deviations[var][u]=all_deviations[var][u]+1
            else:
##                all_deviations[var][u]=[i]
                all_deviations[var][u]=1
    data=[[i.keys(),[j]*len(i.keys())] for i,j in zip(all_deviations.values(),all_deviations.keys())]
    ###plot the data with pylab
    fig=plt.figure(figsize=(22.62372, 12))
    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=.10)
    fig.subplots_adjust(left=.07)
    fig.subplots_adjust(right=1.0)
    fig.subplots_adjust(top=.99)
    hex_data_x=[]
    hex_data_y=[]
    for line in data:
        for i,j in zip(line[0],line[1]):
            for count in range(all_deviations[j][i]):
                hex_data_x.append(i)
                hex_data_y.append(j)
    scatter_data=[]
    counts={}
    for i,j in zip(hex_data_x,hex_data_y):
        counts[(i,j)]=counts.get((i,j),0)+1
    total=float(sum(counts.values()))
    image=plt.scatter([i[0] for i in counts.keys()],[i[1] for i in counts.keys()],c=[i/total*100 for i in counts.values()],\
               cmap=plt.cm.gray_r,s=80)
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
    ax.set_xlim(.98,5.02)
    ax.set_ylim(-.02,2.3)
    plt.savefig('umbrella_sim.svg')
    plt.show()
    cb = plt.colorbar(image)
    plt.savefig('cbar.svg')

run(6,10)

