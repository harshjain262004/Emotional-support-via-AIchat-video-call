from flask import Flask, render_template, request, redirect, url_for, session,flash
from bot import get_Chat_response,get_1st
from sql import *

app = Flask(__name__)
app.secret_key = "chatbotEMU"

@app.route("/")
def index():
    return redirect(url_for("signup"))
    
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_login(username,password):
            session["user"] = username
            session["userid"] = get_userid(username,password)
            session["1r"] = 0
            flash("Succesful Login")
            return redirect(url_for("chat_page"))
        else:
            flash("Incorrect credentials or account does not exist")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if add_signup(username,password):
            flash("Account created successfully")
            return redirect(url_for("login"))
        else:
            flash("Account already exists, Try logging in")
            return render_template('login.html')
    else:
        return render_template('signup.html')

@app.route("/chat",methods=['POST','GET'])
def chat_page():
    if "user" in session:
        if session["1r"]==0:
            userid = session["userid"]
            flash(get_1st(userid))
            return render_template('chat.html')
        else:
            session["1r"] += 1
            return render_template('chat.html')
    else:
        flash("Please Log in to access")
        return redirect(url_for("login"))

@app.route("/chat/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_Chat_response(input,int(session["userid"]))

@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user",None)
        flash("You have been Logged out")
    return redirect(url_for("index"))

@app.route("/templates/WEB_UIKITS.html")
def joincall():
    return render_template('WEB_UIKITS.html')

        
if __name__ == '__main__':
    app.run(debug=True)