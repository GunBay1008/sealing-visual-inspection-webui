from flask import Flask, render_template, request, redirect, url_for
import ssl

ssl._create_default_https_context = ssl._create_unverified_context()

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1008, debug=True)
