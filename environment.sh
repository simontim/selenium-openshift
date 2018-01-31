#!/bin/bash
virtualenv ocp
source ocp/bin/activate
pip install -r requirements.txt
py.test
