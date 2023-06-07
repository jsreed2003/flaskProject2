import os
import time
import datetime
import logging

from flask import Flask, jsonify, render_template



app = Flask(__name__, template_folder='templates')


os.environ["TZ"] = "America/Chicago"
time.tzset()
BUILD = 'Build 20213.0.5 Tue, 30.May.2023, 3:20:09 PM UTC'

# insure the log file exists - create it need be...

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(ROOT_DIR, 'gsimobile.log')
HTML_PATH = os.path.join(ROOT_DIR, 'templates/public')
IMAGE_PATH = os.path.join(ROOT_DIR, 'static/images')

# delete the existing log file and recreate

log_filename = LOG_PATH
if os.path.exists(log_filename):
    os.remove(log_filename)

os.makedirs(os.path.dirname(log_filename), exist_ok=True)

FORMAT = '%(asctime)-15s %(message)s'

logging.basicConfig(format=FORMAT,
                    filename=LOG_PATH,
                    level=logging.DEBUG)

logging.info("********************** app log handler set up **************************")

@app.route('/')
def home():
    return render_template('public/index.html')

@app.route('/offline.html')
def offline():
    return app.send_static_file('offline.html')


@app.route('/serviceworker.js')
def sw():
    return app.send_static_file('serviceworker.js')

@app.route('/comingsoon')
def comingsoon():
    return render_template('public/underconstruction.html')


########## MATERIALS FOR DC ELECTRONICS COURSE ##########
@app.route('/resources')
def resources():
    return render_template('public/page-resources.html')

@app.route('/training')
def training():
    return render_template('public/page-training.html')

@app.route('/courses')
def courses():
    return render_template('public/page-courses.html')

@app.route('/DC-electronics')
def dcelectronics():
    return render_template('public/page-dc-electronics.html')

@app.route('/DC-electronics-ch1')
def dcch1():
    return render_template('public/page-dc-ch1')


########## Error Handler ###########
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    logging.info("Expired link or nonexistent page requested")

    return render_template('public/page-error-4.html'), 404


#if __name__ == '__main__':
#    app.run()
