# -*- coding：utf-8 -*-
# &Author  AnFany

import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

# 多Y轴、刻度不同
xdata = np.linspace(-2, 2, 2000)

y1_data = np.sin(xdata)

y2_data = np.cos(xdata)

y3_data = y1_data + y2_data


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = plt.subplots(figsize=(6, 4))
fig.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
par2.spines["right"].set_position(("axes", 1.2))
make_patch_spines_invisible(par2)
par2.spines["right"].set_visible(True)

# 绘图
p1, = host.plot(xdata, y1_data, "b-", label="Sin(X)", linewidth=2)
p2, = par1.plot(xdata, y2_data, "r-", label="Cos(X)", linewidth=2)
p3, = par2.plot(xdata, y3_data, "g-", label="Sin(X) + Cos(X)", linewidth=2)

#  设置各个轴的名称
host.set_xlabel("X")
host.set_ylabel("Sin(X)")
par1.set_ylabel("Cos(X)")
par2.set_ylabel("Sin(X) + Cos(X)")

#  获得各个线颜色
host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

#  对轴上的数字设置不同颜色
tkw = dict(size=4, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
host.tick_params(axis='x', **tkw)

#  图例
lines = [p1, p2, p3]
host.legend(lines, [l.get_label() for l in lines], loc='upper left')

# 题目
plt.title('多轴不同颜色对比图')

plt.show()

