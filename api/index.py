from flask import Flask
import logging
import os

LOG_FILE_NAME = "flasklogs.log"

# Create and configure logger
logging.basicConfig(filename=LOG_FILE_NAME,
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


app = Flask(__name__)

 
# Test messages
logger.debug("Started server")

@app.route('/')
def home():
    return 'Namaste bhauuu'

@app.route('/echo')
def echo():
    return "Echo"

@app.route("/logs")
def logs():
    if os.path.exists(LOG_FILE_NAME):
        with open(LOG_FILE_NAME, "r") as f:
            return f.read()
    else:
        return "No log file found."