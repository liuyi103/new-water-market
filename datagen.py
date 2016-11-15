# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 21:31:10 2014

@author: liuyi103
"""

import sys
import numpy as np
import random
n=10
if len(sys.argv)>1:
    n=int(sys.argv[1])
print n
voldist=[]
exec 'voldist='+file('voldist.txt','r').readline()
voldist=np.array(voldist)/float(np.sum(voldist))
topos=[[float(j) for j in i.split()]for i in file('realloc.txt','r')]
pos=[np.array(topos[i]) for i in np.random.randint(0,len(topos),n)]
p=np.random.uniform(0.15,0.25,n)
q=(np.random.choice(50,n,p=voldist)+np.random.random(n)-0.5)*20000
sell=np.random.randint(0,2,n)
m=0
f=file('data.txt','w')
f.write('n=%d\n'%n)
for i in range(n):
    f.write('g.add_node(%d)\n'%i)
    f.write('sell[%d],p[%d],q[%d],pos[%d]=%d,%lf,%lf,[%lf,%lf]\n'%(i,i,i,i,sell[i],p[i],q[i],pos[i][0],pos[i][1]))
for i in range(n):
    for j in range(n):
        if sell[i]==1 and sell[j]==0 and np.sum((pos[i]-pos[j])**2)<80 and p[i]<p[j]:
            m+=1
            f.write('g.add_edge(%d,%d)\n'%(i,j))
            f.write('th[%d,%d]=th[%d,%d]=min(q[%d]/3,q[%d]/3)\n'%(i,j,j,i,i,j))
f.write('m=%d\n'%m)
f.close()

