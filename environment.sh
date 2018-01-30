#bin/sh

virtualenv ocp
source bin/activate
pip install pytest
py.test
