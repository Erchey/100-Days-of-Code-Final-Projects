from flask import Flask, render_template
import requests

# posts = requests.get("https://api.npoint.io/4fd68aac02b8d7330eac").json()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


app.run(debug=True)