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
f=trans(1)
t1,t2,t3,t4=0,0,0,0
# t1=time.time()
# prob=cp.Cplex()
# prob.variables.add([0]*m,types=[prob.variables.type.binary]*m)
# prob.variables.add([1 for i in range(m)],[0]*m,types=[prob.variables.type.continuous]*m)
# prob.objective.set_sense(prob.objective.sense.maximize)
# prob.linear_constraints.add([[[f[i,j]for j in range(n) if g.has_edge(i,j)],[1.0 for j in range(n) if g.has_edge(i,j)]]for i in range(n)],'L'*n,[q[i] for i in range(n)])
# prob.linear_constraints.add([[[f[j,i]for j in range(n) if g.has_edge(j,i)],[1.0 for j in range(n) if g.has_edge(j,i)]]for i in range(n)],'L'*n,[q[i] for i in range(n)])
# prob.linear_constraints.add([[[f[i[0],i[1]],x[i[0],i[1]]],[1,-th[i[0],i[1]]]]for i in edges],'G'*m,[0]*m)
# prob.linear_constraints.add([[[f[i[0],i[1]],x[i[0],i[1]]],[1,-min(q[i[0]],q[i[1]])]]for i in edges],'L'*m,[0]*m)
# prob.solve()
#t2=time.time()
#file('vol2.txt','a').write(str(prob.solution.get_objective_value())+'\n')
#t3=time.time()
prob=cp.Cplex()
#p[edges[i][1]]-p[edges[i][0]]
prob.variables.add([0]*m,types=[prob.variables.type.binary]*m)
prob.variables.add([p[edges[i][1]]-p[edges[i][0]] for i in range(m)],[0]*m,types=[prob.variables.type.continuous]*m)
prob.objective.set_sense(prob.objective.sense.maximize)
prob.linear_constraints.add([[[f[i,j]for j in range(n) if g.has_edge(i,j)],[1.0 for j in range(n) if g.has_edge(i,j)]]for i in range(n)],'L'*n,[q[i] for i in range(n)])
prob.linear_constraints.add([[[f[j,i]for j in range(n) if g.has_edge(j,i)],[1.0 for j in range(n) if g.has_edge(j,i)]]for i in range(n)],'L'*n,[q[i] for i in range(n)])
prob.linear_constraints.add([[[f[i[0],i[1]],x[i[0],i[1]]],[1,-th[i[0],i[1]]]]for i in edges],'G'*m,[0]*m)
prob.linear_constraints.add([[[f[i[0],i[1]],x[i[0],i[1]]],[1,-min(q[i[0]],q[i[1]])]]for i in edges],'L'*m,[0]*m)
prob.solve()
t4=time.time()
file('res2.txt','a').write(str(prob.solution.get_objective_value())+'\n')
# file('flow2.txt','a').write(str(sum(prob.solution.get_values()[m:]))+'\n')

#file('time2.txt','a').write('%lf\n'%(t4-t3))
# prob=pp.LpProblem('lyc',pp.LpMaximize)
# xx=pp.LpVariable.dict('a',range(m),cat=pp.LpBinary)
# ggg=pp.LpVariable.dict('b',range(m),0)
# class trans:
#    def __init__(self,case):
#        self.map={}
#        self.case=case
#        pp=0
#        for i in range(n):
#            for j in range(n):
#                if g.has_edge(i,j):
#                    self.map[i*n+j]=pp
#                    pp+=1
#    def __getitem__(self,x):
#        try:
#            return self.case and ggg[self.map[x]] or xx[self.map[x]]
#        except:
#            return 0
# f=trans(1)
# x=trans(0)
# prob+=pp.lpSum([f[i*n+j]*(p[j]-p[i]) for i in range(n) for j in g[i]])
# # print th[2,4],q
# for i in range(n):
#    if sell[i]:
#        prob+=pp.lpSum([f[i*n+j]for j in range(n) if g.has_edge(i,j)])<=q[i]
#    else:
#        prob+=pp.lpSum([f[j*n+i]for j in range(n) if g.has_edge(j,i)])<=q[i]
#    for j in range(n):
#        if g.has_edge(i,j):
#            prob+=f[i*n+j]-x[i*n+j]*th[i,j]>=0,''
#            prob+=f[i*n+j]-x[i*n+j]*max(q[i],q[j])<=0,''
# prob.solve()
# flow = 0
# for i in range(n):
#     for j in g[i]:
#         flow += pp.value(f[i*n+j])
# print flow
# file('flow2.txt','a')
