# @Time  : 2022/01/23 14:54
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
# 被测代码
# 计算器


class Calc:
    def add(self, a, b):

        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a + b

    def div(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a / b