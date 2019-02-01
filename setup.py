# -*- coding: utf-8 -*-

import os
import re
import codecs
from setuptools import setup, find_packages, Command
from setuptools.command.install import install
import matplotlib as mpl
import glob
import os.path
import sys


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


class CustomInstall(install):
    """
    Also copy over the matplotlib files
    """
    def run(self):
        install.run(self)

    
# https://packaging.python.org/guides/single-sourcing-package-version/
def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open(os.path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()


setup(
    name="easydarkfigs",
    version=find_version('easydarkfigs', '__init__.py'),
    install_requires=['matplotlib', 'IPython'],
    packages=find_packages(),
    license='LICENSE',
    author="Ben Cook",
    author_email="bacook17@gmail.com",
    description="iPython Magic for Easy Dark/Light Figures",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="matplotlib, dark figures",
    url="https://github.com/bacook17/easydarkfigs/",
    package_data={'easydarkfigs': ['mplstyles/*.mplstyle']},
    cmdclass={'install': CustomInstall},
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Visualization",
    ]
)
