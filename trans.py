import pydicom
import matplotlib.pyplot as plt
import scipy.misc
import pandas as pd
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import imageio
#.dcm
def Dcm2jpg(file_path,num):
    # 获取所有图片名称
    c = []
    path_a=file_path+"image/"
    path_b=file_path+"image2/"
    if os.path.exists(path_b)==True:
        shutil.rmtree(path_b,True)
    os.mkdir(path_b)
    global names
    if os.path.exists(path_a):
        names = os.listdir(path_a)  # 路径
    else:
        path_a="C:/Users/16941/Desktop/biye/CHUM/HN-CHUM-0"+num+"/PET/CT/image/"
        if os.path.exists(path_a)==True:
            names = os.listdir(path_a)  # 路径
        else:
            return

    # 将文件夹中的文件名称与后边的 .dcm分开
    for name in names:
        index = name.rfind('.')
        name = name[:index]
        c.append(name)

    for files in c:
        picture_path = path_a + files + ".dcm"
        out_path = path_b + files + ".jpg"
        ds = pydicom.read_file(picture_path)
        img = ds.pixel_array  # 提取图像信息

        # plt.imshow(img, "gray")
        # plt.show()

        # imageio.imwrite(out_path, img, 'PNG-FI')
        # scipy.misc.imsave(out_path, img)
        img= (img * 255).astype(np.uint8)  # 转换为0--256的灰度uint8类型
        imageio.imwrite(out_path,img)

    # print('all is changed')



t=65
for i in range (1,t+1):
    if i<10:
        num='0'+str(i)
    else:
        num=str(i)
    path_img='C:/Users/16941/Desktop/biye/CHUM/HN-CHUM-0'+num+'/CT/'
    print(path_img)
    Dcm2jpg(path_img,num)
# #.bmp
# #import scipy.misc
# import os
# from PIL import Image
# def bmp2jpg(file_path,out_path):
# #获取所有图片名称
#     c = []
#     names = os.listdir(file_path) #路径 #将文件夹中的文件名称与后边的 .bmp分开
#     for name in names:
#         index = name.rfind('.')
#         name = name[:index]
#         c.append(name)
#     for files in c :
#         picture_path = "/home/dell/Desktop/unet/d/Mask/"+files+".bmp"
#         out_path = "/home/dell/Desktop/unet/d/Mask1/"+files+"_mask.gif"
#         im = Image.open(picture_path)
#         im.save(out_path)#scipy.misc.imsave(out_path,im)
#     print('all is changed')
# bmp2jpg('/home/dell/Desktop/unet/d/Mask','/home/dell/Desktop/unet/d/Mask1')
