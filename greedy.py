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
f=file('data.txt','r')
for i in f:
    exec i
print m
f.close()
flow = 0
for i in range(n):
    for j in range(n):
        if g.has_edge(i,j):
            tmp=float(min(q[i],q[j]))
            if tmp<th[i,j]:
                continue
            q[i]-=tmp
            q[j]-=tmp
            sw+=tmp*abs(p[i]-p[j])
            flow += tmp
f=file('res1.txt','a')
f.write(str(sw)+'\n')
f.close()
f=file('flow1.txt','a')
f.write(str(flow)+'\n')
f.close()
