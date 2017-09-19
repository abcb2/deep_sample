import numpy as np

"""
theta を右辺から左辺へ移動したのでマイナスが付いたり消えたりしている
"""


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print("AND gate")
    print(AND(0, 0))  # 0
    print(AND(1, 0))  # 0
    print(AND(0, 1))  # 0
    print(AND(1, 1))  # 1

    print("NAND gate ----")
    print(NAND(0, 0))  # 1
    print(NAND(1, 0))  # 1
    print(NAND(0, 1))  # 1
    print(NAND(1, 1))  # 0

    print("OR gate ----")
    print(OR(0, 0))  # 0
    print(OR(1, 0))  # 1
    print(OR(0, 1))  # 1
    print(OR(1, 1))  # 1
