import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute(""" SELECT symbol, SUM(shares) AS totalshares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING totalshares>0""",session["user_id"])

    holdings=[]
    grand_total = 0
    for row in rows:
        stock = lookup(row['symbol'])
        holdings.append({
            "symbol": stock['symbol'],
            "name": stock['name'],
            "shares": row['totalshares'],
            "price": stock['price'],
            "total price": usd(stock['price'] * row['totalshares'])

        })
        grand_total += stock['price'] * row['totalshares']

        rows = db.execute("SELECT cash FROM users WHERE id=?",session["user_id"] )
        cash = rows[0]['cash']


        grand_total += cash
        return render_template("index.html", holdings=holdings,cash=usd(cash),grand_total = usd(grand_total))

    return render_template("index.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("stock"):
            return apology("must provide stock code", 403)
        if not request.form.get("quantity"):
            return apology("must provide quantity", 403)

        stock = request.form.get("stock").upper()

        quantity = int(request.form.get("quantity"))


        check = lookup(stock)

        if check is None:
            return apology("invalid stock code")

        rows = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
        purchase_price = check['price'] * quantity

        cash = rows[0]["cash"]

        if cash < purchase_price:
            return apology("sorry..not enough cash in account")
        else:
            updated_cash = cash - purchase_price

            db.execute("UPDATE users SET cash=:updated_cash WHERE id =:id", updated_cash=updated_cash, id = session["user_id"])

            db.execute(" INSERT INTO transactions(user_id,symbol,shares,price) VALUES(?,?,?,?)",session["user_id"],stock,quantity,check['price'])


            flash("BOUGHT..!")
            return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("provide a symbol", 400)

        symbol = request.form.get("symbol").upper()

        if symbol is None:
            return apology("please provide symbol",400)


        stock = lookup(symbol)
        if stock is None:
            return apology("invalid symbol",400)

        return render_template("quoted.html", stockname={'name':stock['name'],'symbol':stock['symbol'],'price':usd(stock['price'])})


    return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))

        db.execute("INSERT INTO users (username,hash) VALUES(?,?)", username, password)

        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
