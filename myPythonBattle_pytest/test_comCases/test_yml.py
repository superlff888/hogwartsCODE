# @Time  : 2022/01/23 20:06
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
yaml数据驱动
"""
import pytest
import yaml

from Lesson_22.python编程语言与框架.myPythonBattle_pytest_实战.com.calc import Calc


def get_data(pattern, level):
    with open("calc.yml", encoding='UTF-8') as f:  # 编码格式，解决中文乱码
        result = yaml.safe_load(f)
    print(f'\n{type(result)}')
    # result_json = json.dumps(result, ensure_ascii=False, indent=5)  # 调用json模块中的dumps()方法，设置编码格式和缩进方式，然后赋值给变量e
    # print(f'转化为json为 :\n\t{result_json}')
    # print(f'\n{result}')
    # print(f'从yaml文件中读取加法数据：{result.get("add").get("P0").get("datas")}')

    return result.get(pattern).get(level).get("datas"), result.get("add").get("P0").get("ids")  # 调用该函数，获取元组
    # return [result.get(pattern).get(level).get("datas"), result.get("add").get("P0").get("ids")]  # 自定义返回列表


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