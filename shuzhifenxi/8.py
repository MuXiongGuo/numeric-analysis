import numpy as np
import matplotlib.pyplot as plt


# #  定义需要的函数
# def cal_fun(x, y):
#     return x - 30 * y


def Euler_fun(a, b, h, f):
    # f 是目标函数
    # a b是区间始末, 通常来说(b-a)/h应是整除的
    x_list = np.arange(a, b + h, h)
    len = int((b - a) / h)
    y_list_explicit = np.zeros(len + 1)
    y_list_implicit = np.zeros(len + 1)
    # 初值条件
    y_list_explicit[0] = 1
    y_list_implicit[0] = 1
    for i in range(len):
        y_list_explicit[i + 1] = y_list_explicit[i] + h * f(x_list[i], y_list_explicit[i])  # 显式
        y_list_implicit[i + 1] = (y_list_implicit[i] + h*x_list[i + 1])/(1+30*h)  # 隐式  此处的隐式可以直接解出, 如果不能直接解出的话要用迭代法
    return x_list, y_list_explicit, y_list_implicit


# 由不同的h绘制并保存
h_list = [0.1, 0.05, 0.02, 0.01, 0.001, 0.0001]
for index, h in enumerate(h_list):
    x_list, y_list_explicit, y_list_implicit = Euler_fun(0, 10,  h, cal_fun)
    real_value = 901/900*np.exp(-30*x_list)+x_list/30-1/900
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.plot(x_list, real_value, label='real value', linewidth=2, color='k')
    ax.plot(x_list, y_list_explicit, label='explicit', linewidth=1, color='b')
    ax.plot(x_list, y_list_implicit, label='implicit', linewidth=1, color='r')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.grid()
    name = f'Euler and h is {h}'
    plt.title(name)
    plt.savefig(f'{index}.png', dpi=300)