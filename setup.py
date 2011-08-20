# -*- coding: utf-8 -*-
"""
This module contains the tool of cmrs.course
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = open(os.path.join("cmrs", "course", "version.txt")).read().strip()

long_description = (
    read(os.path.join('docs', 'README.txt'))
    + '\n' +
    'Installing\n'
    '**************\n'
    + '\n' +
    read(os.path.join('docs', 'INSTALL.txt'))
    + '\n' +
    'History\n'
    '**********************\n'
    + '\n' +
    read(os.path.join('docs', 'HISTORY.txt'))
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read(os.path.join('docs', 'CONTRIBUTORS.txt'))
    + '\n' +
    'Download\n'
    '********\n')

tests_require = ['zope.testing']

setup(name='cmrs.course',
      version=version,
      description="Courses for the CMRS website",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cmrs', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='cmrs.course.tests.test_docs.test_suite',
      )
