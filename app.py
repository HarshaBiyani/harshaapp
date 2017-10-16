from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import os
app = Flask(__name__)

@app.route('/')
def homepage():
    return "Welcome to API.AI"

@app.route('/test')
def homepage1():
    return "Test page"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0') 
