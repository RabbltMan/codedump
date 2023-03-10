from vector import Vector

positiveSampleList = [Vector(4, 1, 2), Vector(1, 3, 3)]
negativeSampleList = [Vector(2, 2, 4)]
lr = 1
w, b = Vector(0, 0, 0), 0

flag = 0
while (flag == 0):
    error = 0
    for vector in range(len(positiveSampleList)):
        if (w * positiveSampleList[vector] + b) <= 0:
            print(
                f"误分类点 V{vector + 1} = {positiveSampleList[vector]}", end=", ")
            w = w + (lr * positiveSampleList[vector])
            b = b + 1
            error = 1
            print(f"w = {w}, b = {b}")
            break
    if (error == 0):
        for vector in range(len(negativeSampleList)):
            if (-(w * negativeSampleList[vector] + b)) <= 0:
                print(
                    f"误分类点 V{vector + 1 + len(positiveSampleList)} = {negativeSampleList[vector]}", end=", ")
                w = w - (lr * negativeSampleList[vector])
                b = b - 1
                error = 1
                print(f"w = {w}, b = {b}")
                break
    if (error == 0):
        flag = 1
        print(f"没有误分类点, w = {w}, b = {b}")
