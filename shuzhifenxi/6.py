import numpy as np
from sympy import *
import matplotlib.pyplot as plt

def taylor_fun(x):
    return 1+x+x**2/2+x**3/6+x**4/24

x = symbols('x')
pkx = [1,  x, 1.5*x**2-0.5,  2.5*x**3-1.5*x, (35*x**4-30*x**2+3)/8]
coe_cond1 = 0
coe_cond2 = 0
coe_cond3 = 0

#  区间为[-1, 1]
for k in range(5):
    y =pkx[k]
    a = (2*k+1)/2
    z = integrate(a*y*exp(x),(x,-1,1))
    coe_cond1 += z*pkx[k]

#  区间为[-0.1, 0.1]  需要进行缩放
for k in range(5):
    t = 10*x
    pkt = [1, t, 1.5 * t ** 2 - 0.5, 2.5 * t ** 3 - 1.5 * t, (35 * t ** 4 - 30 * t ** 2 + 3) / 8]
    y =pkt[k]
    a = (2*k+1)/2
    z = integrate(10*a*y*exp(t/10),(x,-0.1, 0.1))
    coe_cond2 += z*pkt[k]

#  区间为[-5, 5]  需要进行缩放
for k in range(5):
    t = x/5
    pkt = [1, t, 1.5 * t ** 2 - 0.5, 2.5 * t ** 3 - 1.5 * t, (35 * t ** 4 - 30 * t ** 2 + 3) / 8]
    y =pkt[k]
    a = (2*k+1)/2
    z = integrate(0.2*a*y*exp(5*t),(x,-5, 5))
    coe_cond3 += z*pkt[k]

x_list1 = np.linspace(-5, 5,1000)
x_list2 = np.linspace(-5, 5,1000)
x_list3 = np.linspace(-5, 5,1000)
y_list1 = [float(coe_cond1.evalf(subs={x:el})) for el in x_list1]
y_list2 = [float(coe_cond2.evalf(subs={x:el})) for el in x_list2]
y_list3 = [float(coe_cond3.evalf(subs={x:el})) for el in x_list3]
y_list1_tay = [float(taylor_fun(el)) for el in x_list1]
y_list2_tay = [float(taylor_fun(el)) for el in x_list2]
y_list3_tay = [float(taylor_fun(el)) for el in x_list3]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
ax.plot(x_list1, y_list1, label='[-1,1] Optimal square approximation', linewidth=2, color='b')
ax.plot(x_list1, np.exp(x_list1), label='[-1,1] original function', linewidth=2, color='k')
ax.plot(x_list1, y_list1_tay, label='[-1,1] Taylor', linewidth=2, color='r')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid()
name = 'condition1'
plt.title(name)
plt.savefig('1', dpi=300)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
ax.plot(x_list2, y_list2, label='[-0.1,0.1] Optimal square approximation', linewidth=2, color='b')
ax.plot(x_list2, np.exp(x_list2), label='[-0.1,0.1] original function', linewidth=2, color='k')
ax.plot(x_list2, y_list2_tay, label='[-0.1,0.1] Taylor', linewidth=2, color='r')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid()
name = 'condition2'
plt.title(name)
plt.savefig('2', dpi=300)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
ax.plot(x_list3, y_list3, label='[-5,5] Optimal square approximation', linewidth=2, color='b')
ax.plot(x_list3, np.exp(x_list3), label='[-5,5] original function', linewidth=2, color='k')
ax.plot(x_list3, y_list3_tay, label='[-5,5] Taylor', linewidth=2, color='r')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.grid()
name = 'condition3'
plt.title(name)
plt.savefig('3', dpi=300)
