import matplotlib.pyplot as plt
import os
import numpy as np
#a1,a2=[],[]
rg=range(10,210,10)
ds=len(rg)
# for n in rg:
#     ans1,ans2=0,0
#     for k in range(5):
#         os.system('python datagen.py %d'%n)
#         os.system('python greedy.py')
#         os.system('python opt.py')
#         os.system('python lp.py')
data1=[float(i)for i in file('res1.txt','r').readlines()[-ds*5:]]
data2=[float(i)for i in file('res2.txt','r').readlines()[-ds*5:]]
data3=[float(i)for i in file('res3.txt','r').readlines()[-ds*5:]]
plt.title('Comparison between the social welfares of \noptimal MIP, modified LP and greedy algorithm')
plt.xlabel('number of bids and asks',size=20)
plt.ylabel(r'social welfare $(\times10^5 CNY)$', size = 20)
me1,me2,me3=np.array([np.mean(data1[i*5:i*5+5]) for i in range(ds)]),np.array([np.mean(data2[i*5:i*5+5]) for i in range(ds)]),np.array([np.mean(data3[i*5:i*5+5]) for i in range(ds)])
ma1,ma2,ma3=[np.max(data1[i*5:i*5+5]) for i in range(ds)],[np.max(data2[i*5:i*5+5]) for i in range(ds)],[np.max(data3[i*5:i*5+5]) for i in range(ds)]
mi1,mi2,mi3=[np.min(data1[i*5:i*5+5]) for i in range(ds)],[np.min(data2[i*5:i*5+5]) for i in range(ds)],[np.min(data3[i*5:i*5+5]) for i in range(ds)]
#plt.plot(rg,[np.mean(data1[i*5:i*5+5]) for i in range(20)])
#plt.plot(rg,[np.mean(data2[i*5:i*5+5]) for i in range(20)])
ratio = 1e5
for arr in ['me1', 'me2', 'me3', 'ma1', 'ma2', 'ma3', 'mi1', 'mi2', 'mi3']:
    exec arr+'=np.array('+arr+')/ratio'
plt.errorbar(rg,me1,yerr=[me1-mi1,ma1-me1],label='greedy algorithm')
plt.errorbar(rg,me2,yerr=[me2-mi2,ma2-me2],label='MIP')
plt.errorbar(rg,me3,yerr=[me3-mi3,ma3-me3],label='modified LP')
plt.legend(loc='upper left')
# plt.savefig('compare.pdf', dpi = 1200)
plt.show()
