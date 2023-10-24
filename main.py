"""
This file contains scripts to create a web application using flask
"""

from flask import Flask, render_template, request, redirect, url_for
import ssl

# by-passing the ssl verification
ssl._create_default_https_context = ssl._create_unverified_context()

app = Flask(__name__)

@app.route("/")
def home_page():
    """
    This is a function to render home page
    """
    return render_template('home.html')

@app.route("/training")
def training_page():
    """
    This is a function to render training page
    """
    return render_template('training.html')

@app.route("/detection")
def detection_page():
    """
    This is a function to render detection page
    """
    return render_template('detection.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1008, debug=True)
