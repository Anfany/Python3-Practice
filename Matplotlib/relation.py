# -*- coding：utf-8 -*-
# &Author  AnFany

#  引入库
from matplotlib import colors as mcolors
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl  # 作图显示中文
import os
os.chdir(r'C:\Users\GWT9\Desktop')


#  题目和关键词对应关系字典
prodict = {'s': '数独', 'n': 'N皇后', 'h': '汉诺塔', 'd': '24点', 'm': '幻方', 'p': '完美迷宫', 'c': '凸包', 'o': '一笔画'}
front = 'KaiTi'
#  颜色中去掉轻的，和黑色的
# yanse = np.array([hco for hco in list(mcolors.cnames.keys()) if hco not \
#                   in ['k', 'w', 'whitesmoke', 'floarwhite', 'aliceblue', \
#                       'black', 'seashell', 'ivory', 'ghostwhite', 'beige', 'snow']])
# 选取几种颜色
yanse = ['firebrick', 'royalblue', 'darkgreen', 'darkorange',
         'darkviolet', 'navy', 'indigo', (145/255, 148/255, 198/255)]


#  随机取得位置的函数
def suiji(exdict):
    exlist = np.linspace(1.5, len(exdict) + 0.5, len(exdict))
    np.random.shuffle(exlist)
    return exlist


#  绘制图片
def figure(exdict, ziti=front, secai=yanse):
    weizhi = suiji(exdict)
    zhiwei = suiji(exdict)
    keyd = list(prodict.keys())
    plt.figure(figsize=(5.2, len(exdict) + 1))
    plt.xlim(1, 5.2)
    plt.ylim(1, len(exdict) + 2)
    plt.axis('off')
    for hh in range(len(keyd)):
        #  添加关键字
        mpl.rcParams['font.sans-serif'] = ['%s' % ziti]
        co = yanse[hh % len(secai)]
        plt.text(5, zhiwei[hh], keyd[hh], color=co, size=18)
        #  添加题目
        plt.text(1, weizhi[hh], exdict[keyd[hh]], color=co, size=13)
        #  添加连线
        plt.plot([1 + len(exdict[keyd[hh]]) * 0.23, 5 - 0.1], [weizhi[hh] + 0.08, zhiwei[hh] + 0.08], \
                 color=co, linewidth=2)
    plt.text(1.05, len(exdict) + 1, '题目', size=15)
    plt.text(4.75, len(exdict) + 1, '关键词', size=15)
    plt.title('回复关键词，得到相应谜题')
    plt.savefig(r'.\puzzle.png')
    plt.show()


figure(prodict)



