from setuptools import setup, find_packages

# 会package 有__init__.py的目录
# setup.py根目录中包含__init__.py并没有用,其根目录不会当成一个module 而 helloapp,myapp会当成module

setup(
    name='demo', # package name,对应pip3 uninstall demo
    version='1.0',
    author='cgl',
    author_email='null',
    packages=find_packages(exclude=['*.test', '*.tests.*', 'tests'])
)
