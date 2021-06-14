import sys
sys.path.append("./API Quick Reference")
import API_QuickReference_bot
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index_fn():
    return "Thank you for the visit!!"

@app.route("/api_quick_reference", methods = ['GET', 'POST'])
def api_quick_reference_fn():
    return "Thank you for the visit to API_QR!!"