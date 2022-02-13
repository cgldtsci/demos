from setuptools import setup, Extension, find_packages

# package name, import NAME
NAME = "foo"
VERSION = '1.0.0'
# an Extension instance list
EXT_MODULES = [ 
                Extension(
                    name = 'myprint' 
                    , sources=['src/foo.cpp','src/PythonWrapAPI.cpp']
                    , include_dirs = ['src']
                    )   
                ]   
setup(name = NAME
    , version = VERSION
    , ext_modules = EXT_MODULES
    , )