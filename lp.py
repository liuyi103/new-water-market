# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:44:05 2014

@author: 艺成
"""

import pulp as pp
import networkx as nx
import cplex as cp
import time
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

edges=[(i,j) for i in range(n) for j in range(n)if g.has_edge(i,j)]
class trans:
    def __init__(self,case):
        self.map={}
        self.case=case
        p=0
        for i in range(n):
            for j in range(n):
                if g.has_edge(i,j):
                    self.map[i,j]=p
                    p+=1
    def __getitem__(self,x):
        try:
            return self.case*m+self.map[x[0],x[1]]
        except:
            return 0
x=trans(0)
f=trans(0)
time3=time.time()
prob=cp.Cplex()
prob.variables.add([p[edges[i][1]]-p[edges[i][0]] for i in range(m)],[0]*m,types=[prob.variables.type.continuous]*m)
prob.objective.set_sense(prob.objective.sense.maximize)
prob.linear_constraints.add([[[f[i,j]for j in range(n) if g.has_edge(i,j)],[1.0 for j in range(n) if g.has_edge(i,j)]]for i in range(n)],'L'*n,[q[i] for i in range(n)])
prob.linear_constraints.add([[[f[j,i]for j in range(n) if g.has_edge(j,i)],[1.0 for j in range(n) if g.has_edge(j,i)]]for i in range(n)],'L'*n,[q[i] for i in range(n)])
prob.solve()
f=prob.solution.get_values(0,m-1)
prob.solution.get_values
sw=0
flow = 0
for i in range(m):
    sw+=f[i]>=th[edges[i][0],edges[i][1]] and f[i]*(p[edges[i][1]]-p[edges[i][0]]) or 0
    flow += f[i]>=th[edges[i][0],edges[i][1]] and f[i] or 0
time4=time.time()
file('res3.txt','a').write(str(sw)+'\n')
#file('time4.txt','a').write(str(time4-time3)+'\n')
file('flow3.txt','a').write(str(flow)+'\n')
