import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def gauss_Legendre_8degree(f):
    """f 为函数  返回8节点的结果, 并保留8位有效数字"""
    element_list = [(0.1012285363, 0.9602898565), (0.2223810345, 0.7966664774), (0.3137066459, 0.5255324099), (0.3626837834, 0.1834346425)]
    ans = 0
    for cofficent, root in element_list:
        ans += cofficent*(float(f.evalf(subs={t: root})) + float(f.evalf(subs={t: -1*root})))
    return round(ans, 8)  # 保留8位小数


def gauss_4(f, a, b):
    """四等分区间，复化两点gauss 求积。f 为函数 ab为区间端点"""
    # 四段总和的结果
    res = 0
    # 要求解的四个量
    A0 = symbols('A0')
    A1 = symbols('A1')
    x0 = symbols('x0')
    x1 = symbols('x1')
    # 用来求积分
    x = symbols('x')
    gap_mean = (b - a) / 4
    start, end = a, gap_mean
    # 开始求解
    for i in range(4):
        val_list = []  # 存放4次积分的值
        val_list.append(integrate(1, (x, start, end)))
        val_list.append(integrate(x, (x, start, end)))
        val_list.append(integrate(x**2, (x, start, end)))
        val_list.append(integrate(x**3, (x, start, end)))
        # 解方程得到gauss点和系数
        infor = solve([A0+A1-val_list[0], A0*x0+A1*x1-val_list[1], A0*x0**2+A1*x1**2-val_list[2], A0*x0**3+A1*x1**3-val_list[3]], [A0,A1,x0,x1])
        res += infor[0][0]*f.evalf(subs={u: infor[0][2]})+infor[0][1]*f.evalf(subs={u: infor[0][3]})
        start = end
        end = start+gap_mean
    return float(res)


t = symbols('t')
u = symbols('u')
f1 = pi/2*exp(pi/2*(1+t))*cos(pi/2*(1+t))  # 换元后的方程 即pi/2*f(pi/2*(1+t))
f2 = exp(u)*cos(u)
result1 = gauss_Legendre_8degree(f1)
result2 = gauss_4(f2, 0, float(pi))
print(f'the value of gauss_Legendre_8degree is {result1}')
print(f'the value of gauss two point and divide four is {result2:.8f}')