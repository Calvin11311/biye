import tensorflow as tf
import numpy as np
import pdb
from datetime import datetime
from VGG16 import *
import cv2
import os


# import matplotlib.pyplot as plt

def test(path):
    x = tf.placeholder(dtype=tf.float32, shape=[None, 224, 224, 3], name='input')
    keep_prob = tf.placeholder(tf.float32)
    # 注意更改自己的类别数，此处输出为29类
    output = VGG16(x, keep_prob, 29)
    score = tf.nn.softmax(output)
    # 返回每一行最大置信度所在的索引数组
    f_cls = tf.argmax(score, 1)

    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    # 训练好的模型位置
    saver.restore(sess, './model/model.ckpt-3000')
    for i in os.listdir(path):
        imgpath = os.path.join(path, i)
        im = cv2.imread(imgpath)
        im = cv2.resize(im, (224, 224))  # * (1. / 255)

        im = np.expand_dims(im, axis=0)
        # 测试时，keep_prob设置为1.0
        pred, _score = sess.run([f_cls, score], feed_dict={x: im, keep_prob: 1.0})
        prob = round(np.max(_score), 4)
        # 打印测试图片所属类别的索引号和置信度
        print("{} rubbing class is: {}, score: {}".format(i, int(pred), prob))
        # plt.imshow(im)
        # plt.imshow(im1)
        # plt.title(u'预测值:%i' % pred)
        # plt.show()
    sess.close()


if __name__ == '__main__':
    # 测试图片保存在文件夹中了，图片前面数字为所属类别
    path = './test_img'
    test(path)

