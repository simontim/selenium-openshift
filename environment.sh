#!/bin/bash
virtualenv ocp
source ocp/bin/activate
pip install -r requirements.txt
py.test -v test_zero.py::test_remote
