from collections import Iterable

print(isinstance('wasd',Iterable))
dict1={"name":'张三',"sex":'男','age':20}      # 字典类型的数据
for item in dict1:
    print(item)                          # 输出键名


# 迭 代 器 原 理
class aa:
    def __init__(self):
        self.datas = ['a','b','c','d']
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if (self.index<len(self.datas)):
            val = self.datas[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration
obj=aa()
print(isinstance(obj,Iterable))
for item in obj:
    print(item)

