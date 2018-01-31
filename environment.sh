#!/bin/bash
virtualenv ocp
source ocp/bin/activate
pip install -r requirements.txt
Xvfb :99 &
export DISPLAY=:99
py.test
