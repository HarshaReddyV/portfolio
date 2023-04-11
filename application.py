import os

from cs50 import SQL
from flask import Flask,  redirect, render_template, request


app = Flask(__name__)

db = SQL("sqlite:///reports.db")


@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        p = int(request.form.get("personal"))



        if p > 0 and p < 18200:
            pt =0
        elif p>18200 and p<45000:
            pt = int((p -18200) * 0.19)
        elif p>45000 and p<120000:
            pt = int((p - 45000) * 0.325 + 5092)
        elif p>120000 and p<180000:
            pt = int((p - 120000) * 0.37 + 29467)
        elif p>180000:
            pt = int((p - 180000) * 0.45 + 29467)

        s = int(request.form.get("sole"))

        if s>0 and s < 18200:
            st =0
        elif s>18200 and s<45000:
            st = int((p -18200) * 0.19)
        elif s>45000 and s<120000:
            st = int((s - 45000) * 0.325 + 5092)
        elif s>120000 and s<180000:
            st = int((s - 120000) * 0.37 + 29467)
        elif s>180000:
            st = int((s - 180000) * 0.45 + 29467)

        b = int(request.form.get("business"))

        if b >0:
            bt = int(b * 0.30)

        tt= pt+st+bt


        db.execute("INSERT INTO records(personal_income,sole_income,business_income,total) VALUES(?,?,?,?)", p,s,b,tt)

        allreports = db.execute("SELECT * FROM records ORDER BY id DESC")

        return render_template("report.html", allreports=allreports)


    return render_template("index.html")


