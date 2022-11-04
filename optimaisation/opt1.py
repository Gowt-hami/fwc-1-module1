import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad
#defining function
def f(x):
	return (np.sqrt(x)*np.sin(x))
def f2(x):
        y,e = quad(f, 0, x)
        return y
def f3(x):
    if (np.abs(x)<1e-10):
        res = x
    else:
        res = np.sqrt(x)*np.sin(x)
    return res

X = np.arange(0.5,8,0.01)

def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = quad(f,0,val)
        res[i]=y
    return res
#defining derivative of f(x)
df=lambda x:(np.sqrt(x)*np.sin(x));

#for maxima using gradient ascent
cur_x1=0.5
previous_step_size1=1
iters1=0
precision=0.000000001
alpha=0.0001
max_iters=100000000

while (previous_step_size1>precision)&(iters1<max_iters):
	prev_x=cur_x1
	cur_x1+=alpha*df(prev_x)
	previous_step_size1=abs(cur_x1-prev_x)
	iters1+=1
max_val=f2(cur_x1)
print('maximum value of x is',max_val,"at","x=",cur_x1)

#for minima using gradient ascent
cur_x2=4
previous_step_size2=1
iters2=0

while (previous_step_size2>precision)&(iters2<max_iters):
	prev_x=cur_x2
	cur_x2-=alpha*df(prev_x)
	previous_step_size2=abs(cur_x2-prev_x)
	iters2+=1
min_val=f2(cur_x2)
print('minimum value of x is',min_val,"at","x=",cur_x2)

#Plotting f(x)
X=np.arange(0.5,8,0.01)
#y=F(X)
label_str = "$(√x*sin(x))$"
plt.plot(X,F(X),label='label_str')
#Labelling points
plt.plot(cur_x1,max_val,'o')
plt.text(cur_x1, max_val,f'P({cur_x1:.4f},{max_val:.4f})',label='point maxima')
plt.plot(cur_x2,min_val,'o')
plt.text(cur_x2, min_val,f'Q({cur_x2:.4f},{min_val:.4f})',label='point minima')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.show()
plt.savefig('/sdcard/mgowthami/optimization1/opt1/integ.pdf')
