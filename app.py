from flask import Flask, render_template, request
import json
from Cachehandler import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('form.html')

@app.route('/api', methods=["GET", "POST"])
def api():
    if request.method == "POST":
        c = request.get_data()
        d = c.decode("utf8")
        ClearCache('cache.txt')
        WriteCache('cache.txt', d)

    else:
        if ReadCache('cache.txt') != "":
            t = ReadCache('cache.txt')
            return json.loads(t)


if __name__ == '__main__':
    app.run(debug=True)
