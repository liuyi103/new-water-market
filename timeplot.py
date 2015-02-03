# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 21:47:05 2014

@author: 艺成
"""
import matplotlib.pyplot as plt
import os
import numpy as np
rg1=range(100,1000,100)
rg2=range(100,2100,100)
data1=[float(i)for i in file('time1.txt','r').readlines()[:45]]
data2=[float(i)for i in file('time2.txt','r').readlines()[:45]]
data3=[float(i)for i in file('time3.txt','r').readlines()[:100]]
data4=[float(i)for i in file('time4.txt','r').readlines()[:100]]
#plt.title('Running time of  MIP and modified LP \nfor optimizing social welfare and optimimizing trading volume')
plt.xlabel('number of bids and asks',size=20)
plt.ylabel('total trading volume (m^3)')
me1,me2=np.array([np.mean(data1[i*5:i*5+5]) for i in range(9)]),np.array([np.mean(data2[i*5:i*5+5]) for i in range(9)])
me3,me4=np.array([np.mean(data3[i*5:i*5+5]) for i in range(20)]),np.array([np.mean(data4[i*5:i*5+5]) for i in range(20)])
ma1,ma2=[np.max(data1[i*5:i*5+5]) for i in range(9)],[np.max(data2[i*5:i*5+5]) for i in range(9)]
ma3,ma4=[np.max(data3[i*5:i*5+5]) for i in range(20)],[np.max(data4[i*5:i*5+5]) for i in range(20)]
mi1,mi2=[np.min(data1[i*5:i*5+5]) for i in range(9)],[np.min(data2[i*5:i*5+5]) for i in range(9)]
mi3,mi4=[np.min(data3[i*5:i*5+5]) for i in range(20)],[np.min(data4[i*5:i*5+5]) for i in range(20)]
#plt.plot(rg,[np.mean(data1[i*5:i*5+5]) for i in range(20)])
#plt.plot(rg,[np.mean(data2[i*5:i*5+5]) for i in range(20)])
plt.errorbar(rg1,me1,yerr=[me1-mi1,ma1-me1],label='MIP\ntrading volume')
plt.errorbar(rg1,me2,yerr=[me2-mi2,ma2-me2],label='MIP\nsocial welfare')
plt.errorbar(rg2,me3,yerr=[me3-mi3,ma3-me3],label='modified LP\ntrading volume')
plt.errorbar(rg2,me4,yerr=[me4-mi4,ma4-me4],label='modified LP\nsocial welfare')
plt.legend(loc='lower right')
plt.yscale('log')
plt.show()