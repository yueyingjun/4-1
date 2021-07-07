# 生 成 器 原 理
from collections import Iterable
import time
aa=((i for i in range(100)))    # 生成迭代器  动态计算
for item in aa:
    print(item)

# 协 程
def aa():
    # for item in range(10):
    while True:
        yield
        print("我是sa函数")
        time.sleep(1)

def bb():
    # for item in range(10):
    while True:
        yield
        print("我是sb函数")
        time.sleep(1)
one=aa()
two=bb()
while True:
    next(one)
    next(two)