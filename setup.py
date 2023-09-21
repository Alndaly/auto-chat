from setuptools import setup, find_packages

setup(
    name='auto-wechat',

    version='0.0.1',

    description='A personal chat bot',

    url='https://github.com/alndaly/auto-wechat',

    author='KindaHall',
    author_email='1142704468@qq.com',

    license='MIT',

    keywords='wechat itchat api robot weixin personal extend',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=['httpx', 'pyqrcode', 'pypng'],

    # List additional groups of dependencies here
    extras_require={},
)
