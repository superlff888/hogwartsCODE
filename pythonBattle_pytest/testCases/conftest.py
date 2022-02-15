# @Time  : 2022/01/23 19:56
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
【该hook函数作用】
    防止测试用例标题ids中文两乱码
【注意】
    conftest文件必须放在包中（包含init.py文件）
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


# # 动态生成log文件的名称 (可以不在pytest.ini文件中设置日志文件了)
def pytest_configure(config):
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    config.option.log_file = os.path.join(config.rootdir, '../logs', f'{time_now}.log')


@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calc()
    yield calc
    print("结束计算")


@pytest.fixture(scope='module', autouse=True)
def final_over():
    print("测试开始")
    yield
    print("测试结束")
