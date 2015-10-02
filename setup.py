#!/usr/bin/env python
# -*- coding: utf-8 -*

from distutils.core import setup
import os


def get_packages(package):
    """
    Return root package & all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='randomavatar',
    version='0.4.2',
    packages=get_packages('randomavatar'),
    package_data=get_package_data('randomavatar'),
    description='Create pastel style avatars from a given string \
        (such as username). Similar to gravatars.',
    author='Richard O\'Dwyer',
    author_email='richard@richard.do',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description='https://github.com/richardasaurus/randomavatar',
    install_requires=['pillow<=2.9.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
