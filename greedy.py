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
for i in range(100):
    for j in range(100):
        if g.has_edge(i,j):
            tmp=float(min(q[i],q[j]))
            if tmp<th[i,j]:
                continue
            q[i]-=tmp
            q[j]-=tmp
            sw+=tmp
f=file('vol1.txt','a')
f.write(str(sw)+'\n')
f.close()

