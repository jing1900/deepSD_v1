from model import SRCNN
from utils import input_setup

import numpy as np
import tensorflow as tf

import pprint
import os

flags = tf.app.flags
flags.DEFINE_integer("epoch", 10000, "Number of epoch [10]")

flags.DEFINE_string("input","label_141","input directory")
flags.DEFINE_string("label","label_141","label directory")
flags.DEFINE_string("feature","dem","feature directory")

flags.DEFINE_integer("input_size", 281, "The size of input image to use[141]")
flags.DEFINE_integer("image_size", 701, "The size of image to use [281]")
flags.DEFINE_integer("label_size", 701, "The size of label to produce [281]")
flags.DEFINE_integer("patch_size", 33, "the size of sub images")
flags.DEFINE_integer("patch_size_l", 21, "the size of sub label images")

flags.DEFINE_integer("batch_size", 100, "The size of batch images [64]")
flags.DEFINE_float("learning_rate", 1e-4, "The learning rate of gradient descent algorithm [1e-4]")
flags.DEFINE_integer("c_dim", 1, "Dimension of image color. [1]")
#flags.DEFINE_float("scale", 3, "The size of scale factor for preprocessing input image [3]")
flags.DEFINE_integer("stride", 16, "The size of stride to apply input image [14]")
flags.DEFINE_string("checkpoint_dir", "checkpoint_281", "Name of checkpoint directory [checkpoint]")
flags.DEFINE_string("sample_dir", "output_281", "Name of sample directory [output30]")
flags.DEFINE_string("log_dir","log_281","Name of tensorboard dir[log]")
flags.DEFINE_boolean("is_train", True, "True for training, False for testing [True]")
FLAGS = flags.FLAGS

pp = pprint.PrettyPrinter()

def main(_):
  pp.pprint(flags.FLAGS.__flags)

  if not os.path.exists(FLAGS.checkpoint_dir):
    os.makedirs(FLAGS.checkpoint_dir)
  if not os.path.exists(FLAGS.sample_dir):
    os.makedirs(FLAGS.sample_dir)

  #gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.4)
  #with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
  with tf.Session() as sess:
    srcnn = SRCNN(sess, 
                  input_size=FLAGS.input_size,
                  image_size=FLAGS.image_size, 
                  label_size=FLAGS.label_size, 
                  batch_size=FLAGS.batch_size,
                  patch_size=FLAGS.patch_size,
                  patch_size_l=FLAGS.patch_size_l,
                  c_dim=FLAGS.c_dim, 
                  checkpoint_dir=FLAGS.checkpoint_dir,
                  sample_dir=FLAGS.sample_dir)

    srcnn.train(FLAGS)
    
if __name__ == '__main__':
  tf.app.run()
