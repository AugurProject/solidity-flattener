#!python3

from setuptools import setup, find_packages

setup(
    name='augur-solidity-flattener',
    description='Flattens Solidity code that uses imports into a single file.',
    author='Eric Huang, BlockCAT Technologies Inc.',
    author_email='team@blockcat.io',
    url='https://github.com/AugurProject/solidity-flattener',
    version='0.2.5',
    packages=find_packages(exclude=["*tests"]),
    scripts=['bin/solidity_flattener']
)
