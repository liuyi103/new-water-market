# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 13:26:43 2014

@author: liuyi103
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pulp as pp
import sys

n=100
if len(sys.argv)>1:
    n=int(sys.argv[0])
g=nx.DiGraph()
pos={}
sell={}
sw=0
q={}
p={}
th={}
#for i in range(n):
#    g.add_node(i)
#    sell[i]=np.random.randint(0,2)
#    pos[i]=np.random.rand(2)
#    q[i]=np.random.rand(1)*5+1
#    p[i]=np.random.rand(1)
#for i in range(100):
#    for j in range(100):
#        if sell[i]==1 and sell[j]==0 and np.sum((pos[i]-pos[j])**2)<0.1 and p[i]<p[j]:
#            g.add_edge(i,j)
f=file('data.txt','r')
for i in f:
    exec i
print m
f.close()
for i in range(100):
    for j in range(100):
        if g.has_edge(i,j):
            tmp=float(min(q[i],q[j]))
            if tmp<th[i,j]:
                continue
            q[i]-=tmp
            q[j]-=tmp
            sw+=tmp*abs(p[i]-p[j])
f=file('res1.txt','w')
f.write(str(sw))
f.close()

