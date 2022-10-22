# -*- codeing=utf-8 -*-
# @Time : 2022/10/20 20:46
# @Author: 曹志阳
# @FALE 阈值算法.py
# @software :PyCharm
import cv2 as cv
import matplotlib.pyplot as plt


# 封装图片显示函数
def image_show ( image ) :
    if image.ndim == 2 :
        plt.imshow ( image , cmap = 'gray' )
    else :
        image = cv.cvtColor ( image , cv.COLOR_BGR2RGB )
        plt.imshow ( image )

    plt.show ( )



# 大津法（OTSU）阈值分割：
# 算法思想：最大类间方差法
# （1）对于给定阈值T，可以将图像分为目标和背景。其中，背景点数占图像比例为P0，平均灰度值为M0。
#     而目标点数占图像比例为P1，平均灰度值为M1。
#     P0 + P1 = 1
# （2）图像的平均灰度值为常数，与阈值无关，即：
#     M_mean = P0 * M0 + P1 * M1
# （3）计算类间方差如下：
#      sigma^2 = P0(M0 -M_mean)^2 + P1(M1 - M_mean)^2
# （4）代入 P0 + P1 = 1 和 M_mean, 化简上式为：
#     sigma^2 = P0 * P1 * (M0 - M1)^2
# （5）遍历灰度值，找出使sigma^2最大的值。


if __name__ == '__main__' :

    # 读取灰度图像
    img_desk = cv.imread ( 'wu1.jpg' , 0 )

    # 初始化最佳类间方差和最佳阈值
    T_best = 0
    sigma_best = -1

    # 通过迭代寻找最佳阈值（最大类间方差）
    for i in range ( 0 , 256 ) :

        # 分别获取背景部分和目标点部分
        back_ground = img_desk [ img_desk <= i ]
        img_object = img_desk [ img_desk > i ]

        # 获取背景点和目标点比例
        P0 = back_ground.size / img_desk.size
        P1 = img_object.size / img_desk.size

        # 获取背景点和目标点的均值
        if back_ground.size == 0 :
            M0 = 0
        else :
            M0 = back_ground.mean ( )

        if img_object.size == 0 :
            M1 = 0
        else :
            M1 = img_object.mean ( )

        # 计算类间方差
        sigma = P0 * P1 * (M0 - M1) ** 2

        # 判断是否更新方差和阈值
        if sigma > sigma_best :
            sigma_best = sigma
            T_best = i

    # 阈值分割
    _ , img_bin = cv.threshold ( img_desk , T_best , 255 , cv.THRESH_BINARY )

    # 输出最佳阈值和最大类间方差
    print ( "最大类间方差 = " , sigma_best )
    print ( "最佳阈值 = " , T_best )

    # 显示图像
    image_show ( img_bin )