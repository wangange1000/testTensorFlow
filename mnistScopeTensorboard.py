# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:20:17 2018

@author: wangange
"""
"""
@code: 1051739153@qq.com
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_inference

# 初始常量
INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500

def train(mnist):
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')
    
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    y = mnist_inference.inference(x, regularizer)
    global_step = tf.Variable(0, trainable=False)
    
    with tf.name_scope("moving_average"):
        variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
        variables_averages_op = variable_averages.apply(tf.trainable_variables())
    
    with tf.name_scope("loss_function"):
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(y, tf.argmax(y_, 1))
        cross_entropy_mean = tf.reduce_mean(cross_entropy)
        loss = cross_entropy_mean + tf.add(tf.get_collection('losses'))
        
    with tf.name_scope("train_step"):
        learning_rate = tf.train.Exponential_decay(LEARNING_RATE_BASE, global_step, mnist.train.num_examples/BATCH_SIZE, LEARNING_RATE_DECAY, stairecase=True)
        train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step = global_step)
        with tf.control_dependencies([train_step, variables_averages_op]):
            train_op = tf.no_op(name='train')
            
    writer = tf.summary.FileWriter("/path/to/log", tf.get_default_graph())
    writer.close()
    
def main(argv=None):
    mnist = input_data.read_data_sets("/path/to/mnist_data", one_hot=True)
    train(mnist)
    
if __name__=='__main__':
    tf.app.run()