import pulp as pp
import networkx as nx
import cplex as cp
import time
n=100
g=nx.Graph()
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
print sell

edges=[(i,j) for i in range(n) for j in range(n)if g.has_edge(i,j)]
edge_num = {x:k for k, x in enumerate(edges)}
alphas = [p[j]-p[i] for i,j in edges]
m = len(edges)

master = cp.Cplex()
master.objective.set_sense(master.objective.sense.minimize)
master.variables.add(obj=[1]*n, lb=[0]*n, ub=[q[i]* 0.2 for i in range(n)])
master.solve()
xs = master.solution.get_values()

helper = cp.Cplex()
helper.variables.add(obj=[-i for i in xs], types=[helper.variables.type.binary]*n, names=['y%d'%i for i in range(n)])
helper.variables.add(obj=alphas, lb=[0]*m, names=['f%d'%i for i in range(m)])
helper.variables.add(types=[helper.variables.type.binary]*m , names=['nz%d'%i for i in range(m)])  # nonzero
helper.objective.set_sense(helper.objective.sense.maximize)
helper.linear_constraints.add(
    [
        [['f%d'%edge_num[i,j] for j in g[i]]+['y%d'%i],
        [1]*len(g[i]) + [-q[i]]]
        for i in range(n) if sell[i]==1],
    ['L' for i in range(n) if sell[i]==1],
    [0 for i in range(n) if sell[i]==1])
helper.linear_constraints.add(
    [
        [['f%d'%edge_num[j,i] for j in g[i]]+['y%d'%i],
        [1]*len(g[i]) + [-q[i]]]
        for i in range(n) if sell[i]==0],
    ['L' for i in range(n) if sell[i]==0],
    [0 for i in range(n) if sell[i]==0])
helper.linear_constraints.add(
    [
        [['f%d'%i, 'nz%d'%i], [1, -th[edges[i][0], edges[i][1]]]]
        for i in range(m)
    ],
    'G'*m,
    [0]*m
)
helper.linear_constraints.add(
    [
        [['f%d'%i, 'nz%d'%i], [1, -1e8]]
        for i in range(m)
    ],
    'L'*m,
    [0]*m
)
helper.solve()
ys = helper.solution.get_values()[:n]
ts = helper.solution.get_objective_value() + sum([ys[i]*xs[i] for i in range(n)])
while helper.solution.get_objective_value() >0.1:
    master.linear_constraints.add([[[k for k,i in enumerate(ys) if i > 0.5],[1 for i in ys if i > 0.5]]], 'G', [ts])
    master.solve()
    xs = master.solution.get_values()
    helper.objective.set_linear([('y%d'%i, -xs[i]) for i in range(n)])
    helper.solve()
    ys = helper.solution.get_values()[:n]
    ts = helper.solution.get_objective_value() + sum([ys[i] * xs[i] for i in range(n)])
    print ts
    print master.solution.get_objective_value()
