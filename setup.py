# #! /usr/bin/env python
# # -*- coding: utf-8 -*-
# """
#     Setup file for vayu.
#     Use setup.cfg to configure your project.

#     This file was generated with PyScaffold 3.2.1.
#     PyScaffold helps you to put up the scaffold of your new Python project.
#     Learn more under: https://pyscaffold.org/
# """
# import sys

# from pkg_resources import VersionConflict, require
# from setuptools import setup

# try:
#     require("setuptools>=38.3")
# except VersionConflict:
#     print("Error: version of setuptools is too old (<38.3)!")
#     sys.exit(1)


# if __name__ == "__main__":
#     setup(use_pyscaffold=True)
#! /usr/bin/env python
"""A template for scikit-learn compatible packages."""


import codecs
import os

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('vayu', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'vayu'
DESCRIPTION = 'Tools for Air Quality Data Analysis.'
with codecs.open('README.md', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Sustainability-Lab@IITGN'
MAINTAINER_EMAIL = 'apoorv.agnihotri@iitgn.ac.in, deepak.narayanan@iitgn.ac.in'
URL = 'https://sustainability-lab.github.io/vayu'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://sustainability-lab.github.io/vayu'
VERSION = __version__
INSTALL_REQUIRES = [
    'matplotlib', 'numpy', 
    'pandas', 'geopandas', 'scipy', 
    'scikit-learn' 
    ]
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7']
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'matplotlib'
    ]
}

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      python_requires='>=3.6')



# import setuptools
# import codecs

# with codecs.open('README.md', encoding='utf-8-sig') as f:
#     long_description = f.read()

# # with open("README.md", "r") as fh:
# #     long_description = fh.read()

# setuptools.setup(
#     name="vayu", # Replace with your own username
#     version="0.0.12",
#     author="Sustainability-Lab@IITGN",
#     author_email="apoorv.agnihotri@iitgn.ac.in",
#     description="Tools for Air Quality Data Analysis",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://sustainability-lab.github.io/vayu/",
#     packages=setuptools.find_packages(),
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     setup_requires=['wheel'],
#     install_requires=[
#         'matplotlib', 'numpy', 
#         'pandas', 'geopandas', 'scipy', 
#         'scikit-learn'],
#     python_requires='>=3.6',
# )