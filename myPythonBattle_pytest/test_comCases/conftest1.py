# @Time  : 2022/01/23 19:56
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


"""
防止测试用例标题ids中文两乱码
"""

