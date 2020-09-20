from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

#referencing this file
app = Flask(__name__)
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] =False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column( db.String(100))
    email = db. Column( db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


#pass the url string
@app.route("/")
#define the function for the route
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method =="POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login Successful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged in")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email=None
    if "user" in session:
        user = session["user"]
        
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()

            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("not logged in")
        return redirect(url_for("login"))
        

@app.route('/logout')
def logout():
    if "user" in session:
        user = session["user"]
        flash ("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    
    return redirect(url_for("login"))
# @app.route("/test")
# #define the function for the route
# def test():
#     return render_template("new.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


# def home():
#     return "Hello! this is the main page <h1> HELLO</h1>"

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# @app.route("/admin/")
# def admin():
#     # if a:
#     return redirect(url_for("user", name="Admin!")






