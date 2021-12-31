import os

from cs50 import SQL
from flask import Flask,  redirect, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        personal = request.form.get("personal")
        sole = request.form.get("sole")
        business = request.form.get("business")


    return render_template("index.html")