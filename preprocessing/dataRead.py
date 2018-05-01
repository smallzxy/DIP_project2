# -*- coding: utf-8 -*-
# @Time    : 2018/4/30 14:17
# @Author  : Intgrp

import os
import pandas as pd
import matplotlib.pyplot as plt
import drop_plastic
import copy

def file_name(file_dir='../dataset'):
    '''
    d读取图片集各个水果名称和该水果的所有图片集
    :param file_dir:dataset的文件路径，为../dataset
    :return:水果文件名列表，各水果文件的所有image名称组成的list，并把所有水果的list合在一个list里

    fruitsName=['丰水梨', '冰糖心苹果', '冰糖橙', '台湾青枣', '国产青苹果', '大台农芒', '富士王',
    '小台农芒', '泰国香蕉', '海南香蕉', '澳洲大芒', '澳洲蜜柑', '特级红富士', '番石榴', '百香果',
     '砀山梨', '米蕉', '纽荷脐橙', '脆肉瓜', '花牛红苹果', '蜜梨', '贡梨', '陕西香酥梨', '雪梨', '鸭梨', '黄金梨']

     fruitsImages=[['../dataset/丰水梨/20170308103252.jpg', '../dataset/丰水梨/20170308103301.jpg',
                    '../dataset/丰水梨/20170308103306.jpg'...],..,[....]]
    '''
    fruitsName = os.listdir(file_dir)#获取dataset下的所有目录，即所有水果名称
    fruitsImages = []
    for dir in fruitsName:
        for root, dirs, files in os.walk(file_dir+'/'+dir):#组合成各个水果目录名称，用于获取其水果所有图片名
            tmp=[]
            for file in files:
                tmp.append(root+'/'+file)
            fruitsImages.append(tmp)
    return fruitsName,fruitsImages

def image2data(fruitsImages):
    '''
    将原始的fruitsImages里面每个水果对应一个list的所有图片转变成
    把26个水果按照序号变成0-25进行标记，然后对fruitsImages所有数据
    变成标准的数据和对应label的格式，转变成DataFrame的格式输出
    :param fruitsImages:
    :return:df
    '''
    result =[]
    
    print("=============图片数据开始加载============")
    for i in range(fruitsImages.__len__()):
        print("正在读取第"+str(i)+"种水果图片")
        for j in range(len(fruitsImages[i])):
            print("读取第"+str(i)+"种水果第"+str(j)+"张图片")
            img = plt.imread(fruitsImages[i][j])
            #图片预处理，提取出里面的水果部分mask，输出水果部分图像out
            mask = drop_plastic.fruit_collect(img)
            [n,m,c]=img.shape
            out = copy.deepcopy(img)
            for k in range(n):
                for l in range(m):
                    out[k][l][0] = out[k][l][0]*mask[k][l]
                    out[k][l][1] = out[k][l][1]*mask[k][l]
                    out[k][l][2] = out[k][l][2]*mask[k][l]
            result.append([fruitsImages[i][j],out,i])
    df = pd.DataFrame(result,columns=['impath','image','label'])
    print("=============图片数据加载成功============")
    return df

def singleImage2Data(imagepath):
    result =[]
    for j in range(len(fruitsImages[i])):
        print("读取第"+str(i)+"种水果第"+str(j)+"张图片")
        img = plt.imread(fruitsImages[i][j])
        #图片预处理，提取出里面的水果部分mask，输出水果部分图像out
        mask = drop_plastic.fruit_collect(img)
        [n,m,c]=img.shape
        out = copy.deepcopy(img)
        for k in range(n):
            for l in range(m):
                out[k][l][0] = out[k][l][0]*mask[k][l]
                out[k][l][1] = out[k][l][1]*mask[k][l]
                out[k][l][2] = out[k][l][2]*mask[k][l]
        result.append([fruitsImages[i][j],out,i])
    return result
    

if __name__ == '__main__':
    print(os.getcwd())#获取当前目录
    fruitsName,fruitsImages = file_name()
    # print(fruitsName)
    # print(fruitsImages)
    df = image2data(fruitsImages)
    # print(df)


#((mask[k][l]==True)?1:0)