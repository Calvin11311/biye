import skimage
import tensor as tf
import numpy as np
###1.Filp将图像进行翻转操作
#You can perform flips by using any of the following commands, from your favorite packages. Data Augmentation Factor = 2 to 4x
# NumPy.'img' = A single image.
def get_img(path):
    return path


for i in range(1,66):
    path="C://Users//16941//Desktop//毕业设计//CHUM//HN-CHUM-0"
    if(i<10):
        path=path+'0'+i+"//CT//RTS//RTSS.mat"
    else:
        path=path+'i'+"//CT//RTS//RTSS.mat"
    height=105
    width=105
    channels=1#通道数 描述图像的几维数据
    img=get_img(path)
    flip_1 = np.fliplr(img)
    # TensorFlow. 'x' = A placeholder for an image.
    shape = [height, width, channels]
    x = tf.placeholder(dtype = tf.float32, shape = shape)
    flip_2 = tf.image.flip_up_down(x)
    flip_3 = tf.image.flip_left_right(x)
    flip_4 = tf.image.random_flip_up_down(x)
    flip_5 = tf.image.random_flip_left_right(x)


###2.Rotation将图像进行旋转操作
# Placeholders: 'x' = A single image, 'y' = A batch of images
# 'k' denotes the number of 90 degree anticlockwise rotations
for i in range(1,66):
    path="C://Users//16941//Desktop//毕业设计//CHUM//HN-CHUM-0"
    if(i<10):
        path=path+'0'+i+"//CT//RTS//RTSS.mat"
    else:
        path=path+'i'+"//CT//RTS//RTSS.mat"
    height=105
    width=105
    channels=1#通道数 描述图像的几维数据
    batch=100
    img=get_img(path)
    shape = [height, width, channels]
    x = tf.placeholder(dtype = tf.float32, shape = shape)
    rot_90 = tf.image.rot90(img, k=1)
    rot_180 = tf.image.rot90(img, k=2)
    shape = [batch, height, width, 3]
    y = tf.placeholder(dtype = tf.float32, shape = shape)
    rot_tf_180 = tf.contrib.image.rotate(y, angles=3.1415)
    rot = skimage.transform.rotate(img, angle=45, mode='reflect')


###3.Scale将图像进行放缩
# Scikit Image. 'img' = Input Image, 'scale' = Scale factor
# For details about 'mode', checkout the interpolation section below.
scale_out = skimage.transform.rescale(img, scale=2.0, mode='constant')
scale_in = skimage.transform.rescale(img, scale=0.5, mode='constant')
# Don't forget to crop the images back to the original size (for
# scale_out)


###4.Crop截取部分图像
# TensorFlow. 'x' = A placeholder for an image.
new_height=55
new_width=55
original_size = [height, width, channels]
x = tf.placeholder(dtype = tf.float32, shape = original_size)
# Use the following commands to perform random crops
crop_size = [new_height, new_width, channels]
seed = np.random.randint(1234)
x = tf.random_crop(x, size = crop_size, seed = seed)
output = tf.images.resize_images(x, size = original_size)



###5.Translation沿xy轴移动图像
# pad_left, pad_right, pad_top, pad_bottom denote the pixel
# displacement. Set one of them to the desired value and rest to 0
shape = [batch, height, width, channels]
x = tf.placeholder(dtype = tf.float32, shape = shape)
# We use two functions to get our desired augmentation
x = tf.image.pad_to_bounding_box(x, pad_top, pad_left, height + pad_bottom + pad_top, width + pad_right + pad_left)
output = tf.image.crop_to_bounding_box(x, pad_bottom, pad_right, height, width)


###6.Gaussian Noise
#TensorFlow. 'x' = A placeholder for an image.
shape = [height, width, channels]
x = tf.placeholder(dtype = tf.float32, shape = shape)
# Adding Gaussian noise
noise = tf.random_normal(shape=tf.shape(x), mean=0.0, stddev=1.0,
dtype=tf.float32)
output = tf.add(x, noise)·