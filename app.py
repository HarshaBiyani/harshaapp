from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import os, json
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to API.AI"

@app.route('/test')
def homepage1():
    return "Test page"

@app.route('/webhook',methods=["POST"])
def homepage2():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    speech = "Hello"
    res = {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
        }
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0') 
