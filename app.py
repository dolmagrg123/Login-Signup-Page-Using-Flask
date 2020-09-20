from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#referencing this file
app = Flask(__name__)
# a= False

#pass the url string
@app.route('/')
#define the function for the route
def index():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    # if a:
    return redirect(url_for("index"))

if __name__ == "__main__":
        app.run(debug=True)





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


