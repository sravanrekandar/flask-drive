call python -m venv env
call env/Scripts/activate

call pip install -r requirements.txt

call set FLASK_APP=app/run.py
call set FLASK_ENV=development

call flask run --port 8085 
