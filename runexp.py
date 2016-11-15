import os

# for n in range(8, 50, 8):
n = 24
for i in range(1000):
    os.system('python datagen.py %d' % n)
    # os.system('python stable.py')
    # os.system('python opt.py')
    os.system('python lp3.py')