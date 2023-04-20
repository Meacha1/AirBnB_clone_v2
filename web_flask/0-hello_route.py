#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello HBNB!"
