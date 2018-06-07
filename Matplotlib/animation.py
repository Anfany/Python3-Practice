#  # -*- coding：utf-8 -*-
# &Author  AnFany
#  指定存放图片的路径
import os
os.chdir(r'C:\Users\GWT9\Desktop')

import imageio  #  引入制作动画的库

#  需要合成动态图片的图片的名称列表
namelist = ['%s_foldui.jpg' % g for g in range(10)]

#  开始合成动态图片
def create_gif(image_list=namelist, gif_name='animation.gif', gap=0.9):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=gap)  # duration控制动态图中每张图片的显示时间
    return print('合成完毕')

create_gif()
