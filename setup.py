from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from setuptools import find_packages

setup(name='ikfastpy',
      version='0.1.0',
      license='MIT License',
      long_description=open('README.md').read(),
      packages=find_packages(),
      ext_modules=[Extension("ikfastpy", 
                            ["ikfastpy.pyx", 
                             "ikfast_wrapper.cpp"], language="c++", libraries=['lapack'])],
      cmdclass = {'build_ext': build_ext})
