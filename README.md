# Running a Flask App

## Dependencies for my build
- Python 3.7
- pipenv - used for virtual enviroment management
- flask
- blinker
- simplejson
- python-dotenv
- watchdog
- flask-wtf

### Install dependencies
```sh
pipenv install <dependencies>
```

### Activate pipenv
__You must be in virtual environment to run the flask app__
```sh
pipenv shell
```

### Environment Variables for flask app and run
```sh
export FLASK_APP=<flask_app_name>.py
export FLASK_DEBUG=1 #sets it to debug, no need to stop server to see updated changes
flask run
```

### Run debug mode from within the script
```py
if __name__ == 'main':
	app.run(debug=True)
```


