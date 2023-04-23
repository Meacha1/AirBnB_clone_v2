#!/usr/bin/python3
'''A script that starts a Flask web application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    unsoretd_states = storage.all('State')
    states = sorted(unsoted_states.values(), key=lambda x: x.name)
    unsoted_cities = storage.all('City')
    cities = sorted(unsoted_cities.values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states, cities=cities)

@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
