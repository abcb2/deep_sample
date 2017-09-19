def AND(x1, x2):
    """
    ANDゲート
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def NAND(x1, x2):
    """
    Not ANDゲート
    """
    w1, w2, theta = -0.5, -0.5, -0.6
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def OR(x1, x2):
    """
    OR ゲート
    """
    w1, w2, theta = 0.3, 0.3, 0.2
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


if __name__ == "__main__":
    print("AND gate ----")
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
