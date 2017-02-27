#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setuptools config file."""

import pip
from pip.req import parse_requirements
from setuptools import setup, find_packages

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt',
                                  session=pip.download.PipSession())

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='TK17_Tg_Bot',
    version='0.1',
    packages=find_packages(),
    author='Kees Hink',
    author_email="keeshink@gmail.com",
    description="A Telegram Bot for Dutch parliament elections 2017",
    long_description=open("README.md").read(),
    url='',
    license='MIT',
    download_url='',
    keywords=['telegram', 'bot', 'poll'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console ',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Topic :: Utilities',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'run_bot = tk17_tg_bot.__main__:main',
        ],
    },
    install_requires=reqs,
)
