#!/bin/bash
Xvfb :99 &
export DISPLAY=:99
virtualenv ocp
source ocp/bin/activate
pip install -r requirements.txt
py.test
