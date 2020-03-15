#!/bin/bash

echo 'creating virtual environment'
python3 -m venv env

echo 'entering environment'
source env/bin/activate

echo 'installing requirements...'
pip install -r requirements.txt