"""
Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import sys
sys.path.append("./API Quick Reference")
sys.path.append("/home/joeljos/repos/PythonAnywhere-PoCs/API Quick Reference")
import API_QuickReference_bot
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index_fn():
    return "Thank you for the visit!!"

@app.route("/api_quick_reference", methods = ['GET', 'POST'])
def api_quick_reference_fn():
    return API_QuickReference_bot.runme(request)