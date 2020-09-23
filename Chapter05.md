# Flask-Drive Chapter 05: Cleanup environment

To make sure everything is working standalone, delete your flask-drive folder,
Take a git clone, and start the app by using ```start_dev.sh```

If you find something is not working, this is the right time to fix it.

We will enhance the environment.

## Cleaning up requirements.txt

When you did ```pip freeze > requirements.txt```, it added the primary dependencies that you want to include and their dependencies. But you can not maintain the big list.

Let us clean requirements.txt, add only the dependencies that we want to control

```text
Flask==1.1.1
gunicorn==20.0.4
```

## Adding logging to start_dev.sh

```bash
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
```
