# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 13:19
# @Author  : Intgrp

import numpy as np
import matplotlib.pyplot as plt
import os
from skimage import color
from skimage import data,filters

import dataRead as dataRead

def imgShow(img):
    '''
    显示原图
    :param img:
    :return:
    '''
    plt.figure("原图")
    plt.imshow(img)

def rgb2hsvShow(img):
    '''
    将rgb图像转换成hsv空间，并把h、s、v三个空间展示出来
    :param img:
    :return:
    '''
    plt.figure("RGB to HSV")
    hsv = color.rgb2hsv(img)
    hsv *= 255
    hsv.astype(np.uint8)
    plt.subplot(131)
    plt.imshow(hsv[:, :, 0], cmap='gray')
    plt.subplot(132)
    plt.imshow(hsv[:, :, 1], cmap='gray')
    plt.subplot(133)
    plt.imshow(hsv[:, :, 2], cmap='gray')
    plt.show()

def rgb2hist(img):
    '''
    展示该img的RGB三个通道直方图
    :param img: 输入图像
    :return: 输出图像RGB三个通道的直方图
    '''
    plt.figure("hist")
    ar = img[:, :, 0].flatten()
    plt.hist(ar, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)
    ag = img[:, :, 1].flatten()
    plt.hist(ag, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)
    ab = img[:, :, 2].flatten()
    plt.hist(ab, bins=256, normed=1, facecolor='b', edgecolor='b')
    plt.show()

def threshold(image):
    thresh = filters.threshold_otsu(image)  # 返回一个阈值
    #print(thresh)
    #dst = (image >= thresh) * 1.0  # 根据阈值进行分割


    '''
    plt.figure()
    plt.subplot(121)
    plt.title('original image')
    plt.imshow(image, cmap='gray')

    plt.subplot(122)
    plt.title('binary image')
    plt.imshow(dst, cmap='gray')
    plt.show()
    '''

    return thresh

def fruit_collect(img, title="1"):
    '''
    从图片提取出里面的水果部位
    :param img:
    :param name:图片命名
    :return mask:返回出图片水果部位的mask
    '''
    hsv = color.rgb2hsv(img)
    hsv *= 255
    hsv.astype(np.uint8)
    #绘制直方图
    # plt.figure("直方图")
    # ag = hsv[:, :, 1].flatten()
    # plt.hist(ag, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)

    #提取出里面的水果
    thresh = filters.threshold_otsu(hsv[:, :, 1])
    mask = (hsv[:, :, 1] >= thresh)*1.0
    
    '''
    result = color.rgb2gray(img) * mask
    plt.figure(title)
    plt.subplot(121)
    plt.imshow(img,cmap='gray'), plt.title("origin image")
    plt.subplot(122)
    plt.imshow(result,cmap='gray'), plt.title("fruit extract")
    '''

    return mask


if __name__ == '__main__':
    fruitsName, fruitsImages = dataRead.file_name()
    for i in range(0,5):
        img = plt.imread(fruitsImages[i][0])
        fruit_collect(img,i)
    plt.show()














