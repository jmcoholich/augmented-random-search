import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="ars",
    version="1.0",
    author="Jeremiah Coholich",
    author_email="jmcoholich@gmail.com",
    description=("An implementation of augmented random search policy optimization algorithm for gpu-accelerated environments."),
    license="MIT",
    packages=find_packages(),
    long_description=read('README.md'),
)
