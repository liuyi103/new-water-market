# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 22:30:01 2014

@author: liuyi103
"""

import pulp as pp
import networkx as nx
n=100
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
f.close()
prob=pp.LpProblem('lyc',pp.LpMaximize)
x=pp.LpVariable.dict('x',range(n*n),pp.LpBinary)
f=pp.LpVariable.dict('fx',range(n*n),0)
prob+=pp.lpSum([f[i]for i in range(n*n)]),''
for i in range(n):
    if sell[i]:
        prob+=pp.lpSum([f[i*n+j]for j in range(n) if g.has_edge(i,j)])<=q[i],''
    else:
        prob+=pp.lpSum([f[j*n+i]for j in range(n) if g.has_edge(j,i)])<=q[i],''
    for j in range(n):
        if g.has_edge(i,j):
            prob+=f[i*n+j]>=x[i*n+j]*th[i,j],''
            prob+=f[i*n+j]<=x[i*n+j]*max(q[i],q[j]),''
        else:
            prob+=f[i*n+j]==0,''
prob.writeLP('a.lp')
prob.solve()
print pp.value(prob.objective)