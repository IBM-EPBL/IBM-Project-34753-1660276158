import requests
from flask import Flask, render_template
from flask import request, flash, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "secret key"
import ibm_db


conn = ibm_db.connect(
"DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;USERNAME=pwm68393;PASSWORD=z28Q6S76KmFpxRBw;SECURITY=SSL;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt;", "", "")
@app.route("/", methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM users WHERE username =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            insert_sql = "INSERT INTO users VALUES (?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, username)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global userid
    msg = ''
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM users WHERE username =? AND password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)

        if account:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid = account['USERNAME']
            session['username'] = account['USERNAME']

            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

@app.route('/')
def index():

    return render_template("index.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route('/dashboard')
def dashboard():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    cases = {
        'articles': current['articles']


    }

    return render_template("dashboard.html", cases=cases)


@app.route('/Sports')
def Sports():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    cases = {
        'articles': current['articles']


    }

    return render_template("sports.html", cases=cases)


@app.route('/Science')
def Science():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    cases = {
        'articles': current['articles']


    }

    return render_template("science.html", cases=cases)


@app.route('/Entertainment')
def Entertainment():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    cases = {
        'articles': current['articles']


    }

    return render_template("entertainment.html", cases=cases)


@app.route('/Business')
def Business():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    cases = {
        'articles': current['articles']


    }

    return render_template("business.html", cases=cases)


@app.route('/Technology')
def Technology():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    cases = {
        'articles': current['articles']


    }

    return render_template("technology.html", cases=cases)


@app.route('/Login')
def Login():

    return render_template("login.html")


@app.route('/Register')
def Register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)
