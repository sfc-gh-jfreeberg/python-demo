"""
Run `python setup.py install` after activating the Conda environment.
"""

from setuptools import setup, find_packages

setup(
    name="Example Snowpark Python project",
    version="0.1.0",
    packages=find_packages()
)
