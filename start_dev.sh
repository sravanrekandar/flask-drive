#!/bin/bash
python -m venv env
source env/bin/activate

pip install -r requirements.txt

export FLASK_APP=app/run.py
export FLASK_ENV=development

flask run --port 8085 
