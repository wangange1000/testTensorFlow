# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:58:07 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

tf.reset_default_graph()

#import data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

#Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#init_op = tf.initialize_all_variables()
init_op = tf.global_variables_initializer()
saver = tf.train.Saver()

#Train the model and save the model to disk as a model.ckpt file
#file is stored in the same directory as this Python script is started

with tf.Session() as sess:
    sess.run(init_op)
    for i in range(50000):
        batch_xs, batch_ys = mnist.train.next_batch(1)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        
    save_path = saver.save(sess, "D:\\testTensorFlow\\MNIST_data\\model1.ckpt")
    print("Model saved in file: ", save_path)
    sess.close()