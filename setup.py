import re
import os.path
import setuptools
import pkg_resources
from setuptools import setup, find_packages
from setuptools.command.install_lib import install_lib


LICENSE = 'BSD'
CLASSIFIERS = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ]


with open(os.path.join(os.path.dirname(__file__), 'exeamplyCli', '__init__.py')) as f:
    VERSION = re.match(r".*__version__ = '(.*?)'", f.read(), re.S).group(1)


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    DESCRIPION = f.read()

setup(
    name='exeamplyCli',
    version=VERSION,
    description='A project about python cli.',
    long_description=DESCRIPION,
    author='gaosong',
    author_email='m17746591750@163.com',
    packages=find_packages(),
    license=LICENSE,
    classifiers=CLASSIFIERS,
    python_requires='>=3',
    url='www.163.com',
    entry_points={
        'console_scripts': [
            'exeamply_cli=exeamplyCli.exeamplyClid:Cli',
        ],
    }
)


