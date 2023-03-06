from flask import Flask , redirect, url_for , render_template
from index import model

import collections 
import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableSet
    collections.MutableSet = collections.abc.MutableSet
else: 
    from collections import MutableSet



app = Flask(__name__)

k = model()

data = k.get_data()

@app.route("/")
def home():
    return render_template("index.html",rows=k.get_data())


# CATEGORIES
@app.route("/Comedy.html")
def comedy():
    return render_template("Comedy.html",rows=k.get_comedy())

@app.route("/Tech.html")
def tech():
    return render_template("Comedy.html",rows=k.get_tech())

@app.route("/Crime.html")
def crime():
    return render_template("Comedy.html",rows=k.get_crime())

@app.route("/entertainment.html")
def entertainment():
    return render_template("Comedy.html",rows=k.get_entertainment())

@app.route("/Food.html")
def food():
    return render_template("Comedy.html",rows=k.get_food())

@app.route("/Health.html")
def health():
    return render_template("Comedy.html",rows=k.get_health())

@app.route("/Politics.html")
def politics():
    return render_template("Comedy.html",rows=k.get_politics())

@app.route("/Religion.html")
def religion():
    return render_template("Comedy.html",rows=k.get_religion())

@app.route("/Sports.html")
def sports():
    return render_template("Comedy.html",rows=k.get_sports())

@app.route("/Travel.html")
def travel():
    return render_template("Comedy.html",rows=k.get_travel())



if __name__ == '__main__':
    app.run(debug=True)