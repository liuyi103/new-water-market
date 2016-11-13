f1 = file('stable.txt', 'r')
f2 = file('unstable.txt', 'r')

stable = []
unstable = []
for target, f in [(stable, f1), (unstable, f2)]:
    for line in f:
        n, val = line.split()
        target.append(float(val))

for i in range(6):
    maxratio = 1
    for j in range(i*100, i*100+100):
        maxratio = max(maxratio, (stable[j]+1e-6) / (1e-6+unstable[j]))
    print 'when there are %d nodes in the graph, the ratio is up to'% ((i+1)*8),maxratio

for i in range(6):
    diff = 0
    for j in range(i*100, i*100+100):
        if unstable[j] + 0.1 < stable[j]:
            diff += 1
    print 'when %d nodes, from 100 instances, the number of different values is %d' % ((i+1)*8, diff)

for i in range(6):
    print 'total ratio for %d nodes is '%((i+1)*8), sum(stable[i*100: i*100+100])/sum(unstable[i*100: i*100+100])