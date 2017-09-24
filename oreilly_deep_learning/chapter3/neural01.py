# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.pardir)
sys.path.append(os.curdir)

import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("chapter3/sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    """
    入力層を784個(28*28=784)
    出力層を10個(数字0-9のクラス)

    隠れ層1 50個のニューロン
    隠れ層2 100のニューロン
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 配列の形状の推移を確認
    # print(x.shape)  # (784,)
    # print(W1.shape)  # (784, 50)
    # print(W2.shape)  # (50, 100)
    # print(W3.shape)  # (100, 10)
    # exit(0)

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()  # x_test(test_data), t_test(test_label)
network = init_network()
accuracy_cnt = 0
# print(network)
# print(len(x))
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
