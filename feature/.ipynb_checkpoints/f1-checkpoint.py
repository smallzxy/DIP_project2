# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 22:01
# @Author  : Intgrp

import numpy as np
import matplotlib.pyplot as plt
import os
import preprocessing.dataRead as dataRead

def feature_mean_r(imagepath):
    '''
    返回图片RGB的R分量上的颜色均值
    :param img:
    :return:
    '''
    img = plt.imread(imagepath)
    mean_r = np.mean(img[:,:,0])
    return mean_r

def feature_mean_g(imagepath):
    img = plt.imread(imagepath)
    mean_g = np.mean(img[:,:,1])
    return mean_g

def feature_mean_b(imagepath):
    img = plt.imread(imagepath)
    mean_b = np.mean(img[:,:,2])
    return mean_b

def draw_feature(data,title):
    plt.figure(title)
    plt.plot(data[:, 0], color='red')
    plt.plot(data[:, 1], color='green')
    plt.plot(data[:, 2], color='blue')
    plt.show()





#if __name__ == '__main__':

fruitsName, fruitsImages = dataRead.file_name()
df = dataRead.image2data(fruitsImages)
'''
for i in range(0,5):
    statistic = []
    for j in range(0, fruitsImages[i].__len__()):
        img = plt.imread(fruitsImages[i][j])
        mr, mg, mb = feature_mean(img)
        statistic.append([mr, mg, mb])
    a = np.array(statistic)
    draw_feature(a, i)
'''



df['mean_r']=df['image'].apply(lambda x:feature_mean_r(x))
df['mean_g']=df['image'].apply(lambda x:feature_mean_g(x))
df['mean_b']=df['image'].apply(lambda x:feature_mean_b(x))