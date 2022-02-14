# @Time  : 2022/02/10 17:30
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import configparser

"""
封装的原则：
    写死的固定数据（变量），可以封装成类属性，如 配置文件名 config.ini，来控制其他配置文件
    实现某个功能的代码封装成方法，
    在各个方法中都要用到的数据，抽离出来作为实实例属性
封装前，读配置文件数据三部曲：
    conf = configparser.Configparser()  # 实例化
    conf.read('config.ini', encoding='utf8')  # 打开配置文件，然后才可以调用get等方法获取想要的数据
    conf.get(sections, options)  # 获取options数据
"""


class ReadConfig(configparser.ConfigParser):
    def __init__(self, filepath, encoding='utf8'):
        # 执行完此步骤，就可调用父类的成员属性，相当于把父类的__init__方法和成员属性继承过来了；之后用子类实例化一个对象后, 这个对象可以'点'出父类对象的成员属性/方法, 当然也可以'点'出自己类对象的成员属性/方法
        super().__init__()  # （括号中不需要传值self）需要配置父类成员属性，做初始化设置，所以要继承__init__方法
        # 通过子类实例对象（self，即conf）调用父类的方法（read），加载配置文件(可进一步做参数化)
        self.read(filepath, encoding)


conf = ReadConfig('../../conf.ini')  # 需要时，将对象conf导入即可
