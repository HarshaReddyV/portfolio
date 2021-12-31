import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        personal = request.form.get("personal")
        sole = request.form.get("sole")
        business = request.form.get("business")


    return redirect("/")