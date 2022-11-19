import requests
from flask import Flask, render_template
from flask import request, flash, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "secret key"
@app.route('/')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/dashboard')    
def dashboard():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    case= {
        'articles': current['articles']


    }

    return render_template("dashboard.html", cases=case)


@app.route('/Sports')
def Sports():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    case = {
        'articles': current['articles']


    }

    return render_template("sports.html", cases=case)


@app.route('/Science')
def Science():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    case = {
        'articles': current['articles']


    }

    return render_template("science.html", cases=case)


@app.route('/Entertainment')
def Entertainment():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    case = {
        'articles': current['articles']


    }

    return render_template("entertainment.html", cases=case)


@app.route('/Business')
def Business():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    case = {
        'articles': current['articles']


    }

    return render_template("business.html", cases=case)


@app.route('/Technology')
def Technology():

    r = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=e0472fd1e74c4000a79ae6183f775634")
    current = r.json()
    case = {
        'articles': current['articles']


    }

    return render_template("technology.html", cases=case)

@app.route('/logout')
def Logout():
    return render_template("register.html")
if __name__ == '__main__':
    app.run(debug=True)
