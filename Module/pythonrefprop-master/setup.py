# -*- coding: utf-8 -*-
"""
Created on 26.04.2020

@author: Christoph Hoeges
"""
# ======================================================================================================================
#                                                    Imports
# ======================================================================================================================
import setuptools

# ======================================================================================================================
#                                                    Settings
# ======================================================================================================================

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = ["ctREFPROP",
                    "pandas",
                    "numpy",
                    "xlrd",
                    "PySimpleGUI",
                    "matplotlib",
                    "matplotlib-label-lines",
                    "datetime"]

SETUP_REQUIRES = INSTALL_REQUIRES.copy()

setuptools.setup(name="rp_wrapper",
                 version="0.1.6",
                 description="Package to connection python to RefProp and calculate fluid properties.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://git.rwth-aachen.de/EBC/Team_BES/connectors/pythonrefprop",
                 author="Christoph Hoeges",
                 classifiers=["Programming Language :: Python :: 3.6",
                              "Programming Language :: Python :: 3.7", ],
                 packages=["rp_wrapper"],    # setuptools.find_packages(exclude=[""])
                 setup_requires=SETUP_REQUIRES,
                 install_requires=INSTALL_REQUIRES,
                 package_data={'': ['REFPRP64.DLL']},
                 include_package_data=True
                 )
