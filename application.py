import os

from cs50 import SQL
from flask import Flask,  redirect, render_template, request


app = Flask(__name__)

db = SQL("sqlite:///reports.db")


@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        p = request.form.get("personal")
        s = request.form.get("sole")
        b = request.form.get("business")

        db.execute("INSERT INTO records(personal_income,sole_income,business_income) VALUES(?,?,?)", p,s,b)

        return render_template("index.html")


    return render_template("index.html")