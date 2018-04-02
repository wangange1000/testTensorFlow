# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 11:11:17 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os
from tensorflow.examples.tutorials.mnist import input_data

# PROJECTOR需要的日志文件名和地址相关参数
LOG_DIR = 'D:\\testTensorFlow\\'
SPRITE_FILE = 'mnist_sprite.jpg'
META_FILE = "mnist_meta.tsv"

# 使用给出的MNIST图片列表生成sprite图像
def create_sprite_image(images):
    if isinstance(images, list):
        images = np.array(images)
    
    img_h = images.shape[1]
    img_w = images.shape[2]
    # sprite图像可以理解成时所有小图片拼成的大正方形矩阵
    m = int(np.ceil(np.sqrt(images.shape[0])))
    # 全部初始化为1
    sprite_image = np.ones((img_h*m, img_w*m))
    
    for i in range(m):
        for j in range(m):
            # 计算当前图片编号
            cur = i*m+j
            if cur < images.shape[0]:
                # 将当前小图片复制到大图上
                sprite_image[i*img_h:(i+1)*img_h, j*img_w:(j+1)*img_w] = images[cur]
    
    return sprite_image


# 加载MNIST数据，注意one_hot属性
mnist = input_data.read_data_sets("MNIST_data", one_hot=False)
# 生成图像
to_visualise = 1 - np.reshape(mnist.test.images, (-1,28,28))
sprite_image = create_sprite_image(to_visualise)

# 将生成的sprite图像放到相应的日志目录下
path_for_mnist_sprites = os.path.join(LOG_DIR, SPRITE_FILE)
plt.imsave(path_for_mnist_sprites, sprite_image, cmap='gray')
plt.imshow(sprite_image, cmap='gray')

# 生成对应的标签文件
path_for_mnist_metadata = os.path.join(LOG_DIR, META_FILE)
with open(path_for_mnist_metadata, 'w') as f:
    f.write("Index\tLabel\n")
    for index, label in enumerate(mnist.test.labels):
        f.write("%d\t%d\n" % (index, label))