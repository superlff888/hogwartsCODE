# @Time  : 2022/02/15 09:51
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import os
from datetime import datetime


def pytest_configure(config):
    time_now = datetime.now().strftime('%Y%m%d%H%M%S')
    print(config.rootdir)
    config.option.log_file = os.path.join(config.rootdir, './logs', f'{time_now}.log')  # 根目录就最上一级目录吧
