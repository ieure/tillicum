# -*- coding: utf-8 -*-
#
# © 2011, SimpleGeo, Inc All rights reserved.
# © 2012, Ian Eure.
# Author: Ian Eure <ian@simplegeo.com>
#

from setuptools import setup, find_packages

setup(name="tillicum",
      version="0.8.1",
      packages=find_packages(),
      test_suite="nose.collector",
      tests_require=['nose',
                     'mock',
                     'coverage'],
      install_requires=['ostrich'])
