from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector as mysql
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, email, length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret'
Bootstrap(app)
db = mysql.connect(host="localhost", user="root", passwd="", db="enrollment")
cur = db.cursor()

class loginform(FlaskForm):
  username = StringField('Username', validators=[InputRequired(), length(min=4, max=15)])
  password = PasswordField('Password', validators=[InputRequired(), length(min=8, max=80)])
  remember = BooleanField('Remeber me')

@app.route('/login')
def login():
  form = loginform()
  return render_template('login.html')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/students')
def students():
  cur = db.cursor()
  cur.execute("SELECT * FROM students")
  return render_template('students.html', students=cur.fetchall())

@app.route('/addstudent')
def addStudent():
  fname = request.form['fname']
  lname = request.form['lname']
  cur.execute("INSERT INTO students VALUES ('{fname}', '{lname}')")

@app.route('/subjects')
def subjects():
  cur = db.cursor()
  cur.execute("SELECT * FROM subjects")
  return render_template('subjects.html', subjects=cur.fetchall())

@app.route('/professors')
def professors():
  cur = db.cursor()
  cur.execute("SELECT * FROM teachers")
  return render_template('professors.html', professors=cur.fetchall())

@app.route('/pre-enrollment')
def enrollment():
  return render_template('pre-enrollment.html')

@app.route('/ratings')
def ratings():
  return render_template('ratings.html')

if __name__ == '__main__':
  app.run(debug=True)