import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex
p=[-2,3]
x=p[0]
y=p[1]
k=-(3*x-4*y)
print('line equation is 3x-4y+',k)
x=np.linspace(-5,5,100)
y1=(3*x+2)/4
plt.plot(x,y1, '-r',label='3x-4y+2=0')
y2=(3*x+18)/4
plt.plot(x,y2, '-r',label='3x-4y+18=0')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid()
plt.savefig('/sdcard/mgowthami/matrices/fig/par.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/mgowthami/matrices/fig/par.pdf'"))
