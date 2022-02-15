# @Time  : 2022/01/23 19:56
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
【该hook函数作用】
    防止测试用例标题ids中文两乱码
【注意】
    1、conftest文件必须放在包中（包含init.py文件）
    2、所有同级目录运行前都会先执行conftest.py文件，作用域为当前目录及以下，放在根目录下作用域最大
"""
import os
from datetime import datetime

import pytest

from pythonBattle_pytest.src.calc import Calc


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return: None
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 动态生成log文件的名称 (可以将pytest.ini文件中日志保存路径注释掉)
def pytest_configure(config):
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    print(f'\n\n根目录为{config.rootdir}\n\n\n')
    # config.rootdir 配置文件的根目录（根目录为D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest）
    config.option.log_file = os.path.join(config.rootdir, 'testCases/logs',
                                          f'{time_now}.log')  # 根目录就最上一级目录吧；'testCases/logs'是字符串


@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calc()
    yield calc
    print("结束计算")


@pytest.fixture(scope='module', autouse=True)
def final_over():
    print("测试开始")
    yield '测试中'
    print("测试结束")
