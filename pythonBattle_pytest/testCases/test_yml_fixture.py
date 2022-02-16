# @Time  : 2022/01/23 20:06
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
yaml数据驱动
"""
import logging

import pytest
from pythonBattle_pytest.common.getData import get_data
from pythonBattle_pytest.common.get_logger_conf import logger


# from pythonBattle_pytest.src.calc import Calc


class TestCalcYaml:
    # 将yaml文件中获取的数据放在类变量中
    add_p0_data, add_p0_ids = get_data(
        r"D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\data\calc.yml", "add",
        "P0")  # 解包 get_data()所在文件为参考点
    add_p1_data, add_p1_ids = get_data(
        r"D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\data\calc.yml", "add", "P1")  # 解包
    add_p2_data, add_p2_ids = get_data(
        r"D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\data\calc.yml", "add", "P2")  # 解包

    # def setup(self):
    #     self.calc = Calc()

    @pytest.mark.run(order=1)
    # 解决ids乱码，不能同时添加conftest.py和pytest.ini,一山不容二虎
    @pytest.mark.parametrize('a, b ,exc_a', add_p0_data, ids=add_p0_ids)
    def test_yml_0(self, a, b, exc_a, get_calc):
        self.calc = get_calc
        result_a = self.calc.add(a, b)  # 通过fixture函数获取calc，然后将calc转化为成员变量
        # assert result_a == exc_a
        pytest.assume(result_a == exc_a)

    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a, b ,exc_a', add_p1_data, ids=add_p1_ids)
    def test_yml_1(self, a, b, exc_a, get_calc):
        self.calc = get_calc
        result_a = self.calc.add(a, b)
        pytest.assume(result_a == exc_a)

    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('a,b,exc_a', add_p2_data, ids=add_p2_ids)
    def test_yml_2(self, a, b, exc_a, get_calc):
        # eval("")将字符串转成对象(==类对象)
        # 捕获with上下文管理器下代码块发生的异常,该情况下可以不做断言
        with pytest.raises(eval(exc_a)) as exc_info:  # 应传入一个或一组(数组)异常对象，而不是str(如“TypeError”);
            # pytest.raises((ArithmeticError, ZeroDivisionError, ValueError))
            # 产生该级别日志；会不会收集要看logger收集器的级别,会不会展示到文件和控制器要看各自handler的级别
            logging.debug(f'捕获的异常场景为 {eval(exc_a)}')  # eval(exc_a) == TypeError 对象
            self.calc = get_calc  # 将获取的calc转化为成员变量
            self.calc.add(a, b)

        # print(eval(exc_info.typename))
        # print(exc_info.type)
        # print(exc_info.typename)
        # print(exc_a)
        pytest.assume(exc_info.typename == exc_a)  # 捕获异常 == 期望异常
