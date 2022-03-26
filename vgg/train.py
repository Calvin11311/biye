# coding=utf-8
import tensorflow as tf
# import numpy as np
# import pdb
from datetime import datetime
# from VGG16 import *
import VGG16

# tf.reset_default_graph()

batch_size = 24
lr = 0.0001
n_cls = 2  # 训练时根据自己的类别数更改
max_steps = 15000


def read_and_decode(filename):
    # 根据文件名生成一个队列
    filename_queue = tf.train.string_input_producer([filename])

    reader = tf.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)  # 返回文件名和文件
    features = tf.parse_single_example(serialized_example,
                                       features={
                                           'label': tf.FixedLenFeature([], tf.int64),
                                           'img_raw': tf.FixedLenFeature([], tf.string),
                                       })

    img = tf.decode_raw(features['img_raw'], tf.uint8)
    img = tf.reshape(img, [224, 224, 3])
    # 转换为float32类型，并做归一化处理
    img = tf.cast(img, tf.float32)  # * (1. / 255)
    label = tf.cast(features['label'], tf.int64)
    return img, label

def train():
    x = tf.placeholder(dtype=tf.float32, shape=[None, 224, 224, 3], name='input')
    y = tf.placeholder(dtype=tf.float32, shape=[None, n_cls], name='label')
    keep_prob = tf.placeholder(tf.float32)
    output = VGG16.VGG_16(x, keep_prob, n_cls)
    # probs = tf.nn.softmax(output)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output, labels=y))
    # train_step = tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)
    train_step = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(loss)

    accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(output, 1), tf.argmax(y, 1)), tf.float32))

    images, labels = read_and_decode('./train.tfrecords')
    img_batch, label_batch = tf.train.shuffle_batch([images, labels],
                                                    batch_size=batch_size,
                                                    capacity=392,
                                                    min_after_dequeue=200)
    label_batch = tf.one_hot(label_batch, n_cls, 1, 0)
    # log汇总记录
    summary_op = tf.summary.merge_all()

    init = tf.global_variables_initializer()
    # saver = tf.train.Saver()
    saver = tf.train.Saver(max_to_keep=3)
    max_acc = 0
    with tf.Session() as sess:
        sess.run(init)
        train_writer = tf.summary.FileWriter('./logs', sess.graph)
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)
        for i in range(max_steps):
            batch_x, batch_y = sess.run([img_batch, label_batch])
            #            print batch_x, batch_x.shape
            #            print batch_y
            #            pdb.set_trace()
            _, loss_val = sess.run([train_step, loss], feed_dict={x: batch_x, y: batch_y, keep_prob: 0.8})
            if i % 10 == 0:
                train_arr = accuracy.eval(feed_dict={x: batch_x, y: batch_y, keep_prob: 1.0})
                print("%s: Step [%d]  Loss : %f, training accuracy :  %g" % (datetime.now(), i, loss_val, train_arr))
                # 只指定了训练结束后保存模型，可以修改为每迭代多少次后保存模型
                # if (i + 1) == max_steps:
                # checkpoint_path = os.path.join(FLAGS.train_dir, './model/model.ckpt')
                # saver.save(sess, './model/model.ckpt', global_step=i)
                summary_str = sess.run(summary_op)
                train_writer.add_summary(summary_str, i)
            # 保存最近的3个模型参数
            if train_arr > max_acc:
                saver.save(sess, './model/model.ckpt', global_step=i + 1)
        coord.request_stop()
        coord.join(threads)
        # saver.save(sess, 'model/model.ckpt')


if __name__ == '__main__':
    train()
