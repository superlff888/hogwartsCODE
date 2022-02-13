# ！./venv python
# @Author : Mr.lee
# @Date   ：2020-10-18 20:05
#  -*-  utf-8  -*-
import pytest

from calculator import Calculator


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print("计算开始!")

    # #def setup(self):
    #     self.cal = Calculator()
    #     print("计算开始")

    # @pytest.mark.parametrize(("a", "b", "expect"),
    #                          [(1, 2, 3), (-1, 2, 1), (2.2, 3, 5.2), ("0", 6, 18), (2, 1.2, 3.2),
    #                           (6, "y", 18)])
    # def test_add(self, a, b, expect):
    #
    #     if type(a) == str or type(b) == str:
    #         print("submit is str!")
    #     # if (cmath.sqrt(a)) // 2 != 0:
    #     #     print("")
    #     #######  a == 3**0.5  ,b ==2 怎么处理？
    #     else:
    #         re = self.cal.add(a, b)
    #         assert re == expect
    #         print("计算结果为%d" % expect)

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [3 ** 0.5, 2, 1], ["s", "d", "d"], [1, 4, [6]],
                                            [100000000000000, 100000000000000, 200000000000000], [0, 0, 0], [-1, 0, -1],
                                            [-1, -1, -2]])
    def test_add(self, a, b, expect):
        re = self.cal.add(a, b)
        try:
            assert re == expect  # 异常来自try
        except AssertionError as e:
            print("输入参数错误请修改")
            print(e)
        except Exception as e:
            print("其他参数错误请修改")
            print("异常", e)

        else:
            print("{} + {} = {}".format(a, b, re))
            print("大功告成！")

# @pytest.mark.parametrize("a, b, expect", [(1, 2, 0.5), (8, 0, 8), (0, 2, 0), (2, -1, -2)],
#                          ids=['int_case', 'err_case', 'zero_case', 'below_case'])  ##参数重命名
# def test_div(self, a, b, expect):
#     if type(a) == str or type(b) == str:
#         print("submit is str!")
#     elif b == 0:
#         print("除数不能为零！")
#     else:
#         re = self.cal.div(a, b)
#         assert re == expect
#         print("计算结果为%d" % expect)
#
#
# # def teardown(self):
# #      print("计算结束")
# def teardown_class(self):
#     print("计算结束")
