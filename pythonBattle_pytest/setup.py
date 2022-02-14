# @Time  : 2022/02/14 14:58
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================


"""
通过构建文件setup.py将源码文件打包成一个可以install的包
"""
from setuptools import setup, find_packages  # setuptools构建工具包

with open("README.md", "r", encoding="utf-8") as fh:  # with 上下文管理器，不需要手动 关闭文件；as：用fh来接收打开的文件
    long_description = fh.read()

setup(
    name="pytest_encode",  # 包名称，用于 pip install pytest_encode,即安装时使用的名称，或生成.egg文件（安装包文件，新型文件为.whl文件）的名称
    url="https://github.com/xxx/pytest-encode",  # 源码的地址
    version="1.0",  # 包版本
    author="H.Lee",
    author_email="1310157572@qq.com",
    description="set your encoding and logger",  # 描述信息，包的用途
    long_description=long_description,  # 包用途的详细描述，可放在README.md文件中
    # long_description_content_type="text/markdown",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[  # 分类索引，pip对所属包的分类，便于其他人在pypi.org中搜索到包 https://pypi.org/search/
        "Framework :: Pytest",  # 使用pytest框架
        "Programming Language :: Python",  # 使用python语言
        "Topic :: Software Development :: Testing",  # 主题 :: 软件开发 :: 测试
        "Programming Language :: Python :: 3.9",  # python版本
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    ],
    licence="proprietary",  # 授权证书，专有的
    packages=find_packages(),  # ["pytest_encode"],  # 需要打包的目录列表，通过find_packages()自动找到所有的包（含有init文件），然后import需要的包
    keywords=[  # pip对所属包的分类，包含项目所拥有包的关键字
        "pytest",
        "py.test",
        "pytest_encode",
    ],
    install_requires=[  # 需要安装的依赖包
        'pytest',  # install包时，自动将其依赖包安装
        # 'redis>=2.10.5',
    ],
    enter_points={  # 入口模块或入口函数 , 重要！重要！！重要！！！
        "pytest11": [  # pytest11 查找插件的关键字，固定写法
            "pytest_encode = pytest_encode.main",  # 源码包下的main.py 源码文件,当然main也可以命名为其他名称
        ]
    },
    python_requires=">=3.6",
    zip_safe=False  # 此项需要，否则卸载时报windows error
)
