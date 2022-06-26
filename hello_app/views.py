from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/grid/')
def grid():
    elements = [
        render_template("/clock/clock.html"),
        'Second',
        'Third',
        'Fourth',
        'Fifth',
        'Sixth',
        'Seventh',
        'Eighth',
        'Ninth',
        'Tenth',
        'Eleventh',
        'Twelfth'
    ]
    return render_template('grid.html', elements=elements * 1)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/clock/")
def clock():
    return render_template("/clock/clock.html")

def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
