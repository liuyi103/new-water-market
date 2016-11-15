import networkx as nx
import cplex as cp
import os
import time
n=50
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

import opt
edges = opt.edges
values = opt.prob.solution.get_values()[m:2*m]
alphas = [p[j]-p[i] for i,j in edges]
m = len(edges)


try:
    p = cp.Cplex()
    p.variables.add(lb=[0]*m, names=['gf%d'% i for i in range(m)])
    p.variables.add(lb=[0]*m, names=['gb%d'% i for i in range(m)])
    p.variables.add(obj=[1], lb=[0], names=['beta'])

    for k, (i, j) in enumerate(edges):
        p.linear_constraints.add([[['gf%d' % k, 'gb%d' % k], [1, 1]]], 'L', [alphas[k] * values[k]])
        p.linear_constraints.add(
            [
                [
                    ['gf%d' % kk for kk in range(m) if edges[kk][0] == i]
                    + ['gb%d' % kk for kk in range(m) if edges[kk][1] == j]
                    + ['beta'],
                    [1 for kk in range(m) if edges[kk][0] == i]
                    + [1 for kk in range(m) if edges[kk][1] == j]
                    + [-min(q[i], q[j]) * alphas[k]]
                ]
            ],
            'G',
            [0]
        )

    p.objective.set_sense(p.objective.sense.maximize)
    p.solve()

    print p.solution.get_objective_value()
    file('lp3.txt' ,'a').write('{} {}\n'.format(n, p.solution.get_objective_value()))
    if p.solution.get_objective_value() < 0.999999:
        os.system('cp data.txt counter_example%lf.txt'%time.time())
        os.system('cp data.txt counter_example.txt')
except:
    for k in range(m):
        print edges[k], alphas[k] * values[k]