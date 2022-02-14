# @Time  : 2021/06/08 22:21
# @Author    : House Lee
# -*-coding=utf-8-*-
import logging

from pythonBattle_pytest.common.read_config import conf

logger_name = conf.get('logs', 'logger_name')  # 通过conf获取config.ini配置文件的options
_level = conf.get('logs', 'level').upper()  # 支持大写，要用upper()做大写转化，这样的话配置文件就可以维护成大、小写
sh_level = conf.get('logs', 'sh_level').upper()
fh_level = conf.get('logs', 'fh_level').upper()
log_file_path = conf.get('logs', 'log_file_path').upper()


class MyLogging:
    """
    class新创建实例时，会调用__new__，它主要控制一个新实例的创建,即控制类实例创建的规则（__init__方法可以看作运用该规则初始化一个实例）
    __new__必须要有返回值,返回的是当前类的实例; __new__方法正是创建'这个类实例'的方法
    __new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
    """

    # 定义了实例被初始化的规则
    def __new__(cls, *args, **kwargs):  # cls 类方法 ；通常用self代表实例方法
        """
        定义一个实例，该实例需要被指定收集器级别，低于该级别的日志将不会被收集
        :param level: "DEBUG"/"INFO"/"WARNING"/"ERROR"/"CRITICAL"；可单独设置文件日志级别和控制台日志级别
        :param filename: 日志文件所在路径
        :param args:
        :param kwargs:
        """
        # 创建自己的日志收集器
        my_log = logging.getLogger('my_log')  # 将返回的"my_log"赋值给my_log
        # 设置收集的日志的等级，这里设置为DEBUG（表示只收集DEBUG等级及以上的日志）
        my_log.setLevel(_level)  # 执行my_log.info(),不会打印日志收集，因为等级为debug
        # 创建一个日志输出渠道（输出到控制台）
        l_c = logging.StreamHandler()
        # 设置‘输出到控制台的日志’的级别，该级别若低于收集器的级别，则控制台日志将不会被打印
        l_c.setLevel(sh_level)
        # 创建一个日志输出渠道（输出到文件）处理器
        l_f = logging.FileHandler(log_file_path, encoding='utf-8')
        # 设置‘输出到文件的日志’的级别 ； 该级别若低于收集器的级别，则日志将不会被打印到文件中
        l_f.setLevel(fh_level)
        # 设置日志输出的格式
        # ft = '%(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s - %(message)s',
        # '%Y-%m-%d %H:%M:%S'
        ft = logging.Formatter(
            '%(asctime)s   %(name)s - "%(pathname)s:%(lineno)d" - %(funcName)s - %(levelname)s  %(message)s',
            "%Y-%m-%d %H:%M:%S")
        # 设置渠道（控制台和文件）日志的输出格式
        l_c.setFormatter(ft)
        l_f.setFormatter(ft)
        # 将输出渠道添加到日志收集器中，不管是控制台还是文件，都是要‘收集’的
        my_log.addHandler(l_c)
        my_log.addHandler(l_f)
        return my_log


# logger = MyLogging('ERROR', '../../logs/myLog.log')  # 按照__new__(cls)方法定义的规则初始化一个类对象，所以此时的logger就是my_log

# print(logger)

"""
【区别】
1、__new__ 是在我们调用类名进行实例化时自动调用的，__init__ 是在这个类的每一次实例化对象之后调用的
2、__init__方法只能set（初始化），__new__方法必须get（return一个对象）
3、__new__ 方法创建一个实例之后返回这个实例对象并传递给 __init__ 方法的 self 参数
4、__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数
"""

"""
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
所以，日志级别参数仅支持大写
"""
