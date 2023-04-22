#!/usr/bin/python3
'''test'''
from flask import Flask
from models import storage, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    for key, value in storage.all('State').items():
        return render_template('7-states_list.html', states=value)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
