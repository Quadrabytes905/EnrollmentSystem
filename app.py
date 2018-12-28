from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, email, length
from config import config
import db

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
Bootstrap(app)

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/login', methods=["GET", "POST"])
def checkLogin():
  result = db.authenticateLogin(request.form.get('userID'), request.form.get('userPassword'))
  if len(result) == 1:
    session['userID'] = result[0][0]
    return str(result[0][2])
  else:
    return '0'

@app.route('/home')
def home():
  return render_template('home.html', userDetails=db.getUserDetails(session['userID']))

@app.route('/students')
def students():
  return render_template('students.html', students=db.getStudents())

@app.route('/subjects')
def subjects():
  return render_template('subjects.html', subjects=db.getSubjects())

@app.route('/pre-enrollment')
def enrollment():
  return render_template('pre-enrollment.html')

@app.route('/ratings')
def ratings():
  return render_template('ratings.html')

if __name__ == '__main__':
  app.run(debug=True)