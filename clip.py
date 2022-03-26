# ##jpg剪裁方法
#
# from PIL import Image
# import matplotlib.pyplot as plt
# img=Image.open('C:/Users/16941/Desktop/biye/train/000000.jpg')  #打开图像
# size_img=img.size
# size_x=size_img[0]
# size_y=size_img[1]
# print(size_x,size_y)
# plt.figure("beauty")
# plt.subplot(1,2,1), plt.title('origin')
# plt.imshow(img,"gray")
# plt.axis('off')
#
# file_path="C:/Users/16941/Desktop/biye/train/position.txt"
# with open(file_path) as pos:
#     n=1
#     for l in pos:
#         center=l.split(" ")
#         x_c = float(center[0])
#         y_c = float(center[1])
#         # patch=59
#         x = x_c * size_x
#         y = y_c * size_y
#         w = 29
#         h = 29
#         box = (x, y, x + w, y + h)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
#         roi = img.crop(box)
#         plt.subplot(1, 2, 2)
#         plt.title("roi")
#         plt.imshow(roi, "gray")
#         plt.axis('off')
#         plt.show()
#


# with open(file_path) as pos:
#     center=pos.readline()





import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import os
import shutil
import matplotlib.pyplot as plt
import imageio
#.dcm
def clipjpg(file_path,num):
    # 获取所有图片名称
    listimg = []
    path_a=file_path+"image2/"
    path_b=file_path+"image_clip/"
    #确定存储路径
    if os.path.exists(path_b)==True:
        shutil.rmtree(path_b,True)
    os.mkdir(path_b)
    #确定提取路径
    global names
    if os.path.exists(path_a):
        names = os.listdir(path_a)  # 路径
    else:
        path_a="C:/Users/16941/Desktop/biye/CHUM/HN-CHUM-0"+num+"/PET/CT/image/"
        if os.path.exists(path_a)==True:
            names = os.listdir(path_a)  # 路径
        else:
            return

    #打开标定剪裁中心区域的坐标文件position.txt
    a = []
    pos_path=file_path+"position.txt"
    with open(pos_path) as pos:
        a = pos.read()
        a = a.split("\n")
    # len = len(a) - 1


    # 将文件夹中的文件名称与后边的 .jpg分开
    for name in names:
        index = name.rfind('.')
        name = name[:index]
        listimg.append(name)

    #剪裁图片
    n=0
    for files in listimg:
        picture_path = path_a + files + ".jpg"
        outpath = path_b + files +".jpg"
        img = Image.open(picture_path)  # 打开图像
        # plt.subplot(1,2,1), plt.title('origin')
        # plt.imshow(img,"gray")
        size_img = img.size
        size_x = size_img[0]
        size_y = size_img[1]
        # print(size_x, size_y)
        center=a[n]
        center=center.split(" ")
        print(center[0],center[1])
        x_c = float(center[0])
        y_c = float(center[1])
        # patch=59
        x = x_c * size_x
        y = y_c * size_y
        w = 54
        h = 54
        # print(x_c,size_x,x)
        box = (x, y, x + w, y + h)  # (x, y, x+w, y+h), x,y是裁剪框左上角的坐标， x+w,y+h是右下角的坐标
        clip = img.crop(box)
        # plt.subplot(1,2,2), plt.title('clip')
        # plt.imshow(clip,"gray")
        # plt.show()
        imageio.imwrite(outpath, clip)
        #write img
        n=n+1








t=65
for i in range (44,t+1):
    if i<10:
        num='0'+str(i)
    else:
        num=str(i)
    path_img='C:/Users/16941/Desktop/biye/CHUM/HN-CHUM-0'+num+'/CT/'
    print(path_img)
    clipjpg(path_img,num)
