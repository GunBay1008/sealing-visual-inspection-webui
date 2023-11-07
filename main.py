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

@app.route("/training/yolov8")
def training_yolov8_page():
    """
    This is a function to render training yolov8 page
    """
    return render_template('training_yolov8.html')

@app.route("/training/tfod")
def training_tfod_page():
    """
    This is a function to render training tfod page
    """
    return render_template('training_tfod.html')

@app.route("/detection")
def detection_page():
    """
    This is a function to render detection page
    """
    return render_template('detection.html')

@app.route("/detection/tfod")
def detection_tfod():
    """
    This is a function to render tfod detection page
    """
    return render_template('detection_tfod.html')

@app.route("/detection/yolov8")
def detection_yolov8():
    """
    This is a function to render yolov8 detection page
    """
    return render_template('detection_yolov8.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1008, debug=True)
