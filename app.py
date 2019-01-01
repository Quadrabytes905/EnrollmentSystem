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

# ============ LOGIN =============

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
        '0'

# ============ NAVBAR =============

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/home')
def home():
    try:
        session.get('userID')
        return render_template('home.html', userDetails=db.getUserDetails(session['userID']), classes=db.getStudentClasses(session['userID']))
    except Exception as e:
        return redirect('/')


# @app.route('/subjects')
# def subjects():
#     return render_template('subjects.html', subjects=db.getSubjects())


@app.route('/pre-enrollment')
def enrollment():
    return render_template('pre-enrollment.html', classes=db.getClassesToEnroll(session['userID']))

@app.route('/enrollSubject', methods=['POST'])
def enrollSubject():
    try:
        db.enroll(request.form.get('stubCode'), session['userID'])
        return 'True'
    except:
        return 'False'

@app.route('/ratings')
def ratings():
    return render_template('ratings.html', teachers=db.getTeachers())


# ======== ADMIN ==========
@app.route('/admin')
def admin():
    return render_template('./Admin/Students/index.html')

@app.route('/adminStudents')
def adminStudents():
    return render_template('./Admin/Students/index.html', students=db.getStudents())

@app.route('/adminProfessors')
def adminTeacher():
    return render_template('./Admin/Teachers/teacher.html', teachers=db.getTeachers())

@app.route('/adminClasses')
def adminClasses():
    return render_template('./Admin/Classes/classes.html', classSched=db.getClasses())

@app.route('/adminSubjects')
def adminSubjects():
    return render_template('./Admin/Subject/subject.html', subjects=db.getSubjects())

# ============ STUDENTS =============

@app.route('/addStudent', methods=["GET", "POST"])
def addStudent():
    studentID = request.form.get('id')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    course = request.form.get('course')
    year = request.form.get('year')

    if db.addStudent(studentID, fname, lname, course, year) is True:
        return "success"
    else:
        return "fail"


@app.route('/editStudent', methods=["GET", "POST"])
def editStudent():
    studentID = request.form.get('id')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    course = request.form.get('course')
    year = request.form.get('year')

    if db.editStudent(studentID, fname, lname, course, year) is True:
        return "success"
    else:
        return "fail"

# ============ TEACHER =============

@app.route('/addTeacher', methods=["GET", "POST"])
def addTeacher():
    teacherID = request.form.get('tid')
    tfname = request.form.get('tfname')
    tlname = request.form.get('tlname')

    if db.addTeacher(teacherID, tfname, tlname) is True:
        return "success"
    else:
        return "fail"

@app.route('/editTeacher', methods=["GET", "POST"])
def editTeacher():
    teacherID = request.form.get('tid')
    tfname = request.form.get('tfname')
    tlname = request.form.get('tlname')

    if db.editTeacher(teacherID, tfname, tlname) is True:
        return "success"
    else:
        return "fail"

# ============ CLASSES =============

@app.route('/addClasses', methods=["GET", "POST"])
def addClasses():
    code = request.form.get('code')
    cTid = request.form.get('cTid')
    cSid = request.form.get('cSid')
    sched = request.form.get('sched')
    start = request.form.get('start')
    end = request.form.get('end')

    if db.addClasses(code, cTid, cSid, sched, start, end) is True:
        return "success"
    else:
        return "fail"

@app.route('/editClasses', methods=["GET", "POST"])
def editClasses():
    code = request.form.get('code')
    cTid = request.form.get('cTid')
    cSid = request.form.get('cSid')
    sched = request.form.get('sched')
    start = request.form.get('start')
    end = request.form.get('end')

    if db.editClasses(code, cTid, cSid, sched, start, end) is True:
        return "success"
    else:
        return "fail"

# ============ RATING =============

@app.route('/saveRating', methods=["GET", "POST"])
def saveRating():
    try:
        teacherID = request.form.get('teacherID')
        studentID = session['userID']
        rating = request.form.get('rating')
        comment = request.form.get('comment')

        db.rateTeacher(teacherID, studentID, rating, comment)

        return 'success'
    except:
        return 'failed'


# ======== CATCH EXCEPTIONS ==========
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    return "THIS PAGE DOES NOT EXIST!"


if __name__ == '__main__':
    app.run(debug=True)
