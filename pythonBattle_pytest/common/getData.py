# @Time  : 2022/02/14 15:34
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import yaml


def get_data(filepath, pattern, level):
    with open(filepath, encoding='UTF-8') as f:  # 编码格式，解决中文乱码
        result = yaml.safe_load(f)
    # print(f'\n{type(result)}')
    # print(f'\n{result}')
    # result_json = json.dumps(result, ensure_ascii=False, indent=5)  # 调用json模块中的dumps()方法，设置编码格式和缩进方式
    # print(f'转化为json为 :\n\t{result_json}')
    # print(f'\n{result}')
    # print(f'从yaml文件中读取加法数据：{result.get("add").get("P0").get("datas")}')

    return result.get(pattern).get(level).get("datas"), result.get(pattern).get(level).get("ids")  # 调用该函数，获取元组
    # # return [result.get(pattern).get(level).get("datas"), result.get("add").get("P0").get("ids")]  # 自定义返回列表

