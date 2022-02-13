# @Time  : 2022/01/23 14:57
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
from Lesson_22.python编程语言与框架.myPythonBattle_pytest_实战.com.calc import Calc
import pytest


class TestCalc:
    def setup_class(self):
        print("开始测试")
        self.calc = Calc()  # 转化为成员变量，即全局变量

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    # 类中所有用例执行完毕后，才会被调用
    def teardown_class(self):
        print("结束测试")

    # @pytest.mark.P0
    # @pytest.mark.parametrize('a,b,exc_a', [(1, 1, 2), (-0.01, 0.02, 0.01), (10, 0.02, 10.02), (98.99, 99, 197.99),
    #                                        (99, 98.99, 197.99), (-98.99, -99, -197.99), (-99, -98.99, -197.99)],
    #                          ids=['两个整数相除', '两个正负浮点数相除', '整数与浮点数相除', '有效近似值相加-正1', '有效近似值相加-正2',
    #                               '有效近似值相加-负1', '有效近似值相加-负2'])
    # def test_add(self, a, b, exc_a):
    #     res_a = self.calc.add(a, b)
    #     assert res_a == exc_a
    #
    # @pytest.mark.P1
    # @pytest.mark.parametrize('a,b,exc_d', [(1, 1, 1), (-0.01, 0.02, -0.5), (10, 0.02, 500), (98.99, 99, 197.99),
    #                                        (99, 98.99, 197.99), (-98.99, -99, -197.99), (-99, -98.99, -197.99)],
    #                          ids=['两个整数相加', '两个浮点数相加', '整数与浮点数相加', '有效近似值相加-正1', '有效近似值相加-正2',
    #                               '有效近似值相加-负1', '有效近似值相加-负2'])
    # def test_div(self, a, b, exc_d):
    #     res_d = self.calc.div(a, b)
    #     assert res_d == exc_d

    """
    异常场景
    """

    @pytest.mark.add
    @pytest.mark.P2
    @pytest.mark.parametrize('a,b,exc_a',
                             [(1, 2, 3), (99.01, 0, "参数大小超出范围"), (-99.01, -1, "参数大小超出范围"), (2, 99.01, "参数大小超出范围"),
                              (1, -99.01, "参数大小超出范围"),
                              ('文', 9, pytest.raises((TypeError, ValueError, ArithmeticError))),  # a出现异常，b参数的异常就不抛出了
                              (9.3, '文', pytest.raises((TypeError, ValueError, ArithmeticError)))],
                             ids=['两个整数相加', '浮点和0相加', '两个负浮点数相加', '整数与浮点数相加', '浮点数与整数相加', '含有字符串1',
                                  '含有字符串2'])
    def test_add(self, a, b, exc_a):
        print(f'\ntype(a)为：{type(a)}')
        print(f'type(b)为：{type(b)}')
        print(f'a:{a}')
        print(f'b:{b}')
        if type(b) == str or type(a) == str:
            print('参数含有字符串')
            with exc_a as e:  # 捕获异常
                self.calc.add(a, b)  # 此处如果抛异常了，后面的代码就不执行了
            # print(f'e.type是：{e.type}')
            # assert e.type == TypeError  # 为了断言而断言，所以此处可以不要断言；只需要做异常捕获就可以了
        elif type(a) != str and type(b) != str:
            result_a = self.calc.add(a, b)
            assert result_a == exc_a
            print('\n符合代码逻辑')
        else:
            print("条件没命中")

    """
    eval : 获取并返回表达式结果；也可将字符串转化为对象（例如：类对象）
    """
    def test_a(self):
        print(eval("1+2"))
        print(type("TypeError"))
        print(eval("TypeError"))
        print(type(eval("TypeError")))




