import matplotlib.pyplot as plt
import os
a1,a2=[],[]
for n in range(10,110,10):
    ans1,ans2=0,0
    for k in range(5):
        os.system('datagen.py %d'%n)
        os.system('greedy.py')
        os.system('opt.py')
        ans1+=float(file('res1.txt','r').readline())
        ans2+=float(file('res2.txt','r').readline())
    a1+=[ans1]
    a2+=[ans2]
plt.plot(range(10,110,10),a1)
plt.plot(range(10,110,10),a2)
plt.show()
