from flask import Flask, render_template, url_for, redirect, request, session
from datetime import timedelta
#referencing this file
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

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
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
# @app.route("/test")
# #define the function for the route
# def test():
#     return render_template("new.html")

if __name__ == "__main__":
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




# #initializing a database
# app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# #create a model
# class Todo(db.Model):
#     #setting id column that specifies id of each entry
#     id = db.Column(db.Integer, primary_key=True)

#     #text column called content that holds each task
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db. column(db.DateTime, default=datetime.utcnow)

#     #return string everytime we create a new element
#     def __repr__(self):
#         return '<Task %r>' % self.id


