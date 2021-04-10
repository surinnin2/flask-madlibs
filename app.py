from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    """return home"""

    return render_template("home.html", default_story=story)

@app.route('/', methods=["POST"])
def submit_form():
    """return story"""
    data = request.form
    madlib = story.generate(data)

    return render_template("storypage.html", story_data = data, story_madlib = madlib)
