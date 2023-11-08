"""
This file contains scripts to create a web application using flask
"""

from flask import Flask, render_template, request, redirect, url_for
import ssl
from flask_socketio import SocketIO, emit
import subprocess
import threading
from ultralytics import YOLO
import os
import time
import subprocess
import sys
import io
from contextlib import contextmanager
# import logging
# logging.basicConfig(level=logging.DEBUG)

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# by-passing the ssl verification
ssl._create_default_https_context = ssl._create_unverified_context()

app = Flask(__name__)
socketio = SocketIO(app)


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

@app.route('/start-training', methods=['POST'])
def start_training():
    """
    Route to handle the initiation of YOLOv8 model training.

    This function is called when a POST request is made to the '/start-training' endpoint.
    It retrieves the training parameters and the data file from the request, saves the data file,
    and starts a new thread to begin training the model without blocking the main application thread.

    Returns:
        A tuple containing a message indicating that training has started and the HTTP status code 200.
    """
    data_file = request.files['dataFile']
    print(data_file)
    epochs = request.form['epochs']
    batch_size = request.form['batchSize']
    model_type = request.form['modelType']  # Get the model type from the form data
    
    # Save data.yaml file
    data_file_path = 'yolov8_training_config/data.yaml'
    print(data_file_path)
    data_file.save(data_file_path)
    
    # Start training in a new thread
    threading.Thread(target=train_yolo, args=(data_file_path, epochs, batch_size, model_type)).start()
    #time.sleep(3)
    
    return redirect(url_for('training_yolov8_page'))

# Custom context manager to redirect stdout to a string buffer
@contextmanager
def capture_stdout():
    class EmittingStringIO(io.StringIO):
        def write(self, message):
            # Call the write method of the superclass (StringIO)
            super().write(message)
            # Emit the message in real-time
            socketio.emit('training_output', {'data': message})
            print('training_output', {'data': message})
            print('training_output', {'data': message})
            print('training_output', {'data': message})
            # Force the server to handle other requests and emit the message immediately
            socketio.sleep(0)

    # Replace sys.stdout with an instance of the custom StringIO class
    new_stdout = EmittingStringIO()
    old_stdout = sys.stdout
    sys.stdout = new_stdout
    try:
        yield new_stdout
    finally:
        # Restore the original stdout after exiting the context
        sys.stdout = old_stdout

def train_yolo(data_file_path, epochs, batch_size, model_type):
    """
    Starts the training process for a YOLOv8 model.

    This function initializes the YOLO model with the provided model type and starts the training process.
    After training, it performs validation and emits the training results and validation metrics to the client
    via a Socket.IO event.

    Args:
        data_file_path (str): The file path to the training configuration file (data.yaml).
        epochs (int): The number of epochs to train the model.
        batch_size (int): The batch size to use during training.
        model_type (str): The type of YOLOv8 model to train (e.g., 'yolov8n', 'yolov8s', etc.).

    The function does not return a value; instead, it communicates the results back to the client asynchronously.
    """
    # time.sleep(3)
    # Map the model type to the corresponding model file
    model_files = {
        'yolov8n': 'yolov8n.pt',
        'yolov8s': 'yolov8s.pt',
        'yolov8m': 'yolov8m.pt',
        'yolov8l': 'yolov8l.pt',
        'yolov8x': 'yolov8x.pt',
    }
    model_file = model_files.get(model_type, 'yolov8n.pt')  # Default to yolov8n if not specified

    # Initialize the YOLO model with the selected model file
    model = YOLO(model_file)
    # time.sleep(3)
    # Start the YOLOv8 training process
    with capture_stdout():
        results = model.train(data=data_file_path, epochs=int(epochs), batch=int(batch_size))
        
        # Perform validation
        metrics = model.val()

    # socketio.emit('training_output', {'data': capture_stdout().getvalue()})
    
    # Emit the results and metrics to the client
    # socketio.emit('training_results', {'results': str(results), 'metrics': str(metrics)})
    # Capture the output

    


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
    socketio.run(app, host='0.0.0.0', port=1008, debug=True)
