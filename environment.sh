#!/bin/bash
virtualenv ocp
source ocp/bin/activate
pip install pytest
py.test
