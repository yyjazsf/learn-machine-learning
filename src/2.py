'''
张量--阶
'''

import tensorflow as tf

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
with g.as_default():
    # 0阶
    mammal = tf.Variable("Elephant", tf.string)
    ignition = tf.Variable(451, tf.int16)
    floating = tf.Variable(3.14159265359, tf.float64)
    its_complicated = tf.Variable(12.3 - 4.85j, tf.complex64)

    # 一阶
    mystr = tf.Variable(["Hello"], tf.string)
    cool_numbers = tf.Variable([3.14159, 2.71828], tf.float32)
    first_primes = tf.Variable([2, 3, 5, 7, 11], tf.int32)
    its_very_complicated = tf.Variable(
        [12.3 - 4.85j, 7.5 - 6.23j], tf.complex64)

    # 2 阶
    mymat = tf.Variable([[7], [11]], tf.int16)
    myxor = tf.Variable([[False, True], [True, False]], tf.bool)
    linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
    squarish_squares = tf.Variable([[4, 9], [16, 25]], tf.int32)
    rank_of_squares = tf.rank(squarish_squares)
    mymatC = tf.Variable([[7], [11]], tf.int32)

    # 四阶
    my_image = tf.zeros([10, 299, 299, 3])

    with tf.Session() as sess:
        print(tf.rank(my_image).eval())
