from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

name = "Janith"


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
