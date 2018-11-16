#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for jbiot.

"""

import sys
import os
from setuptools import setup

def readfile(filename):
    with open(filename) as f:
        return f.read()

def find_bins():
    bins = []
    for root,dirs,files in os.walk("./bin"):
        for py in files:
            py = os.path.join(root,py)
            bins.append(py)
    return bins
            
def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          use_pyscaffold=True,
        install_requires=readfile("requirements.txt"),
        scripts=find_bins()
        )


if __name__ == "__main__":
    setup_package()
