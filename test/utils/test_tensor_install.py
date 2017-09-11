import tensorflow as tf

hi = tf.constant('Hi.')
sess = tf.Session()

print(sess.run(hi))



