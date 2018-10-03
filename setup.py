#!/usr/bin/env python
from setuptools import setup, find_packages

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession


install_requires = parse_requirements('requirements.txt', session=PipSession())
dependencies = [str(package.req) for package in install_requires]


from distutils.core import setup

setup(name='hydra-flock-central-controller',
      version='0.0.1',
      include_package_data=True,
      description='A simulation for HYDRA: Central Controller API',
      author='W3C HYDRA development group',
      author_email='public-hydra@w3.org',
      url='https://github.com/HTTP-APIs/hydra-flock-central-controller',
      install_requires=dependencies
      )
