#!/usr/bin/env python3

from os import path
import os
import sys

# We assume the directory structure is as follows:
# .../github/pyprobml/ -- location of this file
# .../github/pyprobml/pmtk3/data -- actually a submodule, so 'git submodule init && git submodule update' to get it

print("welcome to pmtk3 python code")
PMTK_PYTHON_DIR = path.dirname(path.abspath(__file__))
PMTK_DIR = path.join(PMTK_PYTHON_DIR, 'pmtk3')
# GITHUB_DIR = path.dirname(PMTK_DIR)
DATA_DIR = path.join(PMTK_DIR, 'data')

# add_dirs = [PMTK_PYTHON_DIR]
# for d in add_dirs:
#     print("Adding {}".format(d))
#     sys.path.append(d)
#     print "Execute this command: export PYTHONPATH=$PYTHONPATH:{}".format(d)