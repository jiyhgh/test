"""
*_* coding: utf-8 *_*
author:ymy
time:2023/2/21 17:01
file :函数复习.py
"""
# def	sum(a,b):
#     return a+b
# sum(2, 5)
# 查看函数文档的方法
help(sum)


def a(x,y):
    b = x+y
    # print(b)
a(100,1000)
# 在控制台输入自定义数字
# input是控制台输入内容
def y():
    c = int(input("请输入数字："))
    d = int(input("请输入数字："))
    e = c + d
    print(e)
y()
def y():
    c = input("请输入数字：")
    d = input("请输入数字：")
    if c.isdigit() and d.isdigit():
        # isdigit()查看输入的内容是否为数字
        s = int(c) + int(d)
        # 如果不是数字进行强转
        print(s)
    else:
        print(f"输入数据有误{c}{d}")
y()
def user_info(name, age, gender):
    # 进行拼接
    print(f'您的名字是{name},年龄是{age}, 性别是{gender}')
user_info(name='xiaoliang', age=20, gender='男')
# 调用函数时，如果有位置参数时，位置参数必须在关键字参数的面前，但关键字参数之间不存在先后顺序
# user_info('小明', gender='男', age=16)
# user_info()
# 缺省参数
def user_info(name, age, gender='男'):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
user_info('xiaoliang', '20', '男')    # 默认参数
# 调用函数时可不传该默认参数的值
user_info('PiuPiu', '20')
# 不定长参数
# 1.动态位置传参
def user_info(*args):
    print(args)
user_info('Piu')
user_info('Piu', 20)
# 2.动态关键词传参
def user_info(**kwargs):
    print(kwargs)
user_info(name='Piu', age=18, id=120)  # 注意kwargs是字典类型，动态关键字传参的结果是一个字典
# 按位置传参和按关键字传参
# 匿名函数
# 1.匿名函数的应用场景
lst = [lambda x: x**2, lambda x: x**2, lambda x: x**2]
for f in lst:
    print(f(9))

