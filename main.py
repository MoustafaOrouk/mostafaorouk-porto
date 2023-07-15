from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date

app = Flask(__name__)


@app.route('/')
def portfolio():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
