from flask import Flask, render_template, request, redirect, url_for

app = Flask('app')
app.debug = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

app.run(host='0.0.0.0', port=8080)