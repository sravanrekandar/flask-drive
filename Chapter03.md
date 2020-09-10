# Flask-Drive Chapter 03: Automating Development: Auto Reload Using Flask

_[Reference Article](https://dev.to/lukeinthecloud/python-auto-reload-using-flask-ci6)_

It is a tedious job that each time you make some changes to the app,
you need to restart the application.
To circumvent this problem, we will use

- Environmental Variables
- flask command

## Setting environmental variables

### For Unix based systems

```bash
(env) $ export FLASK_APP=app.py
(env) $ export FLASK_ENV=development
```

### For windows

```bat
(env) > set FLASK_APP=app.py
(env) > set FLASK_ENV=development
```

### Starting the app

```bash
(env) $ flask run --port 8085
 * Serving Flask app "app/run.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:8085/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 157-488-096
```

Now you can navigate to [http://127.0.0.1:8085/](http://127.0.0.1:8085/)

### Making changes in Home Page contents

Make some small changes in you home page content. Eg: Add your name in the paragraph

```python
"""
<body>
    {nav}
    <h1>{title}</h1>
    <p>This is Sravan's home page.</p>
</body>
"""
```

Now without restarting the process you can go to browser and refresh"Ctrl/Cmd + R". You can see the changes on the page.

## Keeping the app start commands in a file (Unix Systems)

create a file called ```start_dev.sh```

```bash
#!/bin/bash

export FLASK_APP=app.py
export FLASK_ENV=development

flask run --port 8085
```

### Enabling the file to get executed

This is a single time operation

```bash
(env) $ chmod 777 start_dev.sh
```

### Run the app using the start script

```bash
(env) $ ./start_dev
```

## Keeping the app start commands in a file (Windows)

create a file called ```start_dev.bat```

```bash
set FLASK_APP=app.py
set FLASK_ENV=development

flask run --port 8085
```

### Run the app using the start script (Windows)

```bash
(env) $ start_dev.bat
```

## Adding environment activation to automated script ```start_dev.bat```

```bash
#!/bin/bash
python -m venv env
source env/bin/activate

pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_ENV=development

flask run --port 8085
```

Now, each time you use the ```start_dev.bat```,

1. The script checks whether there is an environment
    - If there is not environment, it creates one
    - If there is an environment, it uses it
2. The script tries to install the dependencies
    - If the dependencies already installed, it skips the installation
3. The script now starts the app in debugging mode
    - Each time you make a change in the app code, you need not to restart the app
