# @Time  : 2022/02/14 18:50
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import logging.config


def getLogger_conf(filepath, loggers_key):
    logging.config.fileConfig(filepath)  # '../conf/logging.conf'
    conf_logger = logging.getLogger(loggers_key)  # logging.conf中的key
    return conf_logger


logger = getLogger_conf('../conf/logging.conf', 'main')
