import os

from flask import Flask, session, render_template, request
from flask_session import Session
from flask.ext.bcrypt import Bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# bcrypt for hashing passwords
flask_bcrypt = Bcrypt(app)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():

    #get form information
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("pass1")

    #hash password
    pw_hash = flask_bcrypt.generate_password_hash(password).decode("utf-8")
    db.execute("INSERT INTO users ( email, username, pw_hash ) VALUES (:email, :username, :pw_hash)", 
    {"email":email, "username":username, "pw_hash":pw_hash})
    db.commit()
    return "registration successfull!"
