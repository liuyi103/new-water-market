import os

for n in range(8, 50, 8):
    for i in range(100):
        os.system('python datagen.py %d' % n)
        os.system('python stable.py')
        os.system('python opt.py')