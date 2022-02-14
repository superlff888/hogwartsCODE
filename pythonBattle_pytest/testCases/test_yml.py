# @Time  : 2022/01/23 20:06
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
yaml数据驱动
"""
import json

import pytest
import yaml

from pythonBattle_pytest.common.getData import get_data
from pythonBattle_pytest.src.calc import Calc


def test_out():
    print(get_data("add", "P1"))


class TestCalcYaml:
    # 将yaml文件中获取的数据放在类变量中
    add_p0_data, add_p0_ids = get_data("add", "P1")  # 解包
    add_p1_data, add_p1_ids = get_data("add", "P1")  # 解包

    def setup(self):
        self.calc = Calc()

    # 解决ids乱码，不能同时添加conftest.py和pytest.ini,一山不容二虎
    @pytest.mark.parametrize('a, b ,exc_a', add_p0_data, ids=add_p0_ids)
    def test_yml_0(self, a, b, exc_a):
        result_a = self.calc.add(a, b)
        assert result_a == exc_a

    @pytest.mark.parametrize('a, b ,exc_a', add_p1_data, ids=add_p1_ids)
    def test_yml_1(self, a, b, exc_a):
        result_a = self.calc.add(a, b)
        assert result_a == exc_a