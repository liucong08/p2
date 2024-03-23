# File_name: demo1
# Date: 2024-03-22
class Person:
    def __init__(self):
        self.info = {'username': 'zhangsan'}

    def __getitem__(self, item):  # 通过索引取值
        return self.info[item]
p = Person()
# print(p.info['username'])
print(p['username'])