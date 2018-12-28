from config import config
import mysql.connector as mysql
from mysql.connector import errorcode
import datetime

# Try if system can connect to database
try:
    db = mysql.connect(**config.ConnectionString)
    cur = db.cursor()
except mysql.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


# ============ STUDENTS =============
def getStudents():
    cur.execute("SELECT * FROM students")
    return cur.fetchall()

def addStudents(fname, lname, course, year):
    now = datetime.datetime.now()
    randID = f"{now.year}-{now.month}{now.day}-{now.hour}{now.minute}"
    try:
        cur.execute("INSERT INTO students(studentID, studentFname, studentLname, studentCourse, studentYear) VALUES ('{randID}', '{fname}', '{lname}', '{course}', {year}")
        return True
    except:
        return False

# ============ TEACHERS =============
def getTeachers():
    cur.execute("SELECT * FROM teachers")
    return cur.fetchall()

# ============ SUBJECTS =============
def getSubjects():
    cur.execute("SELECT * FROM subjects")
    return cur.fetchall()

# ============ MISC. =============
def authenticateLogin(username, password):
    cur.execute(f"SELECT * FROM loginusers WHERE userID = '{username}' AND userPassword = '{password}'")
    return cur.fetchall()

def getUserDetails(id):
    cur.execute(f"SELECT * FROM students WHERE studentID = '{id}'")
    return cur.fetchall()
