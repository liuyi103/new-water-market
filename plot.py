import matplotlib.pyplot as plt
import os
import numpy as np
#a1,a2=[],[]
rg=range(10,210,10)
for n in rg:
    ans1,ans2=0,0
    for k in range(5):
        os.system('datagen.py %d'%n)
        os.system('greedy.py')
        os.system('opt.py')
data1=[float(i)for i in file('vol1.txt','r').readlines()[-100:]]
data2=[float(i)for i in file('vol2.txt','r').readlines()[-100:]]
plt.title('Comparsion between the trading volumes of \noptimal MIP and greedy algorithm')
plt.xlabel('number of bids and asks',size=20)
plt.ylabel(r'total trading volume (m^3)')
me1,me2=np.array([np.mean(data1[i*5:i*5+5]) for i in range(20)]),np.array([np.mean(data2[i*5:i*5+5]) for i in range(20)])
ma1,ma2=[np.max(data1[i*5:i*5+5]) for i in range(20)],[np.max(data2[i*5:i*5+5]) for i in range(20)]
mi1,mi2=[np.min(data1[i*5:i*5+5]) for i in range(20)],[np.min(data2[i*5:i*5+5]) for i in range(20)]
#plt.plot(rg,[np.mean(data1[i*5:i*5+5]) for i in range(20)])
#plt.plot(rg,[np.mean(data2[i*5:i*5+5]) for i in range(20)])
plt.errorbar(rg,me1,yerr=[me1-mi1,ma1-me1],label='greedy algorithm')
plt.errorbar(rg,me2,yerr=[me2-mi2,ma2-me2],label='MIP')
plt.legend(loc='upper left')
plt.show()
