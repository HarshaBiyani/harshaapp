from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from flask import Flask, request, make_response
import os, json
app = Flask(__name__)

@app.route('/')
def homepage():
    import sqlite3
    con = sqlite3.connect("sample.db")
    cur = con.cursor()
    cur.execute("create table IF NOT EXISTS sample(name text)")
    cur.execute("insert into sample values('PHarsha')")
    con.commit()
    cur.execute("select * from sample")
    
    data = cur.fetchall()
    
    con.close()
    return "Welcome to API.AI" + "\n\n----\n" + str(data)

@app.route('/test')
def homepage1():
    return "Test page"

@app.route('/webhook',methods=["POST"])
def homepage2():
    req = request.get_json(silent=True, force=True)

    text = req.get("result").get("parameters").get("data")

    speech = ""
    if str(text).lower() == "gn":
        speech = "Good Night"
    elif str(text).lower() == "gm":
        speech = "Good Morning"
    elif str(text).lower() == "ga":
        speech = "Good Afternoon"
    else:
        import urllib
        a = urllib.urlopen("http://www.google.co.in", proxies=None)
        speech = "Hello" + "--->"+str(len(a))

    print("Request:")
    print(json.dumps(req, indent=4))
    
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
