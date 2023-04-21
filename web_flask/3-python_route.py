#!/usr/bin/python3
'''a script that starts a Flask web application.
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''The home page'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''The hbnb page'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''The C page'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/', default={'text': 'is cool'})
def python(text):
    '''The python page'''
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
