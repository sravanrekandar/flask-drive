#!/bin/bash
echo "[FlaskDrive]: A Flask Application"
echo "---------------------------------"
python --version
pip --version
echo "---------------------------------"

echo "[FlaskDrive]: Creating Virtual Environment..."
python -m venv env

echo "[FlaskDrive]: Activating Virtual Environment..."
source env/bin/activate

echo "[FlaskDrive]: Installing Dependencies..."
pip install -r requirements.txt
echo "---------------------------------"

echo "[FlaskDrie]: Starting application..."
export FLASK_APP=app/run.py
export FLASK_ENV=development

flask run --port 8085 
