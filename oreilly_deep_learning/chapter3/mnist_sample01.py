# -*- coding: utf-8 -*-

import sys, os

for _ in (os.pardir, os.curdir):
    sys.path.append(_)

from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)  # (60000, 784)   6万の画像(行）で、784次元(列)
print(t_train.shape)  # (60000, )      6万のラベル(行）で、1次元(列)
print(x_test.shape)  # (10000, 784)
print(t_test.shape)  # (10000, )

print(len(x_train[0]))
print(t_train[0])
print(len(t_train))
