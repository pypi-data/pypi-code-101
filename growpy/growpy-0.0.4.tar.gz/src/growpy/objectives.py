import numpy as np
import tensorflow as tf

class GCNLL(tf.keras.losses.Loss):
    '''
    Negative of the conditional log-likelihood of the
    multivariate Gaussian distribution.
    '''

    def call(self, y_true, y_pred):
        pi = tf.cast(np.pi, dtype=tf.float64)
        n = tf.shape(x, out_type=tf.int64)[1]
        n = tf.cast(n, dtype=tf.float64)
        m = tf.shape(x, out_type=tf.int64)[0]
        m = tf.cast(m, dtype=tf.float64) - 1.
        self.residuals = y_true - y_pred
        self.cov = tf.matmul(
            self.residuals,
            self.residuals,
            transpose_a=True
            )
        self.cov = self.cov / m
        cov_inv = tf.linalg.inv(self.cov)
        cov_det = tf.linalg.det(self.cov)
        self.LL = n * tf.math.log(2 * pi)
        self.LL = tf.math.log(cov_det) + self.LL
        for row in self.residuals:
            prod = tf.tensordot(row, cov_inv, 1)
            prod = tf.tensordot(prod, row, 1)
            self.LL = prod + self.LL
        self.LL = self.LL / 2
        return self.LL
