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
prob = pp.LpProblem('opt',pp.LpMaximize)
f = pp.LpVariable.dict('f', range(m))
