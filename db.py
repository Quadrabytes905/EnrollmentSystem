from config import config
import mysql.connector as mysql
from mysql.connector import errorcode

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


def addStudent(_id, fname, lname, course, year):
    try:
        cur.execute(f"INSERT INTO students VALUES ('{_id}', '{fname}', '{lname}', '{course}', {year})")
        cur.execute(f"INSERT INTO loginusers VALUES ('{_id}','123',2)")
        return True
    except Exception as e:
        return False


def editStudent(id, fname, lname, course, year):
    try:
        cur.execute(f"UPDATE students SET studentFname='{fname}', studentLname='{lname}', studentCourse='{course}', studentYear={year} WHERE studentID='{id}'")
        return True
    except Exception as e:
        return False


# ============ TEACHERS =============
def getTeachers():
    cur.execute("SELECT * FROM teachers")
    return cur.fetchall()

def addTeacher(tid, tfname, tlname):
    try:
        cur.execute(f"INSERT INTO teachers VALUES ('{tid}', '{tfname}', '{tlname}')")
        cur.execute(f"INSERT INTO loginusers VALUES ('{tid}','admin',1)")
        return True
    except Exception as e:
        return 

def editTeacher(tid, tfname, tlname):
    try:
        cur.execute(f"UPDATE teachers SET teacherFname='{tfname}', teacherLname='{tlname}' WHERE teacherID='{tid}'")
        return True
    except Exception as e:
        return False

# ============ MISC. =============
def authenticateLogin(username, password):
    cur.execute(f"SELECT * FROM loginusers WHERE userID = '{username}' AND userPassword = '{password}'")
    return cur.fetchall()


def getUserDetails(id):
    cur.execute(f"SELECT * FROM students WHERE studentID = '{id}'")
    return cur.fetchall()

# ============ CLASSES =============

def getClassesToEnroll(id):
    cur.execute(f"SELECT stubCode, subjectID, schedule, CONCAT(timeStart, ' - ', timeEnd) AS Time, teacherLname, (SELECT COUNT(*) FROM classroll WHERE classroll.stubCode = classes.stubCode AND studentID = '{id}') FROM classes LEFT JOIN teachers ON classes.teacherID = teachers.teacherID")
    return cur.fetchall()


def getStudentClasses(userID):
    cur.execute(f"SELECT classroll.stubCode, classes.subjectID, CONCAT(classes.timeStart, ' - ' , classes.timeEnd) AS Time, classes.schedule, teachers.teacherLname FROM classroll LEFT JOIN classes ON classroll.stubCode = classes.stubCode LEFT JOIN teachers ON classes.teacherID = teachers.teacherID WHERE classroll.studentID = '{userID}'")
    return cur.fetchall()


def enroll(stubCode, userID):
    cur.execute(f"INSERT INTO classroll(stubCode, studentID) VALUES('{stubCode}', '{userID}')")


def getClasses():
    cur.execute("SELECT * FROM classes")
    return cur.fetchall()

def addClasses(code, cTid, cSid, sched, start, end):
    try:
        cur.execute(f"INSERT INTO classes VALUES({code}, '{cTid}', '{cSid}', '{sched}', '{start}', '{end}')")
        return True
    except Exception as e:
        return False

def editClasses(code, cTid, cSid, sched, start, end):
    try:
        cur.execute(f"UPDATE classes SET teacherID='{cTid}',subjectID='{cSid}',schedule='{sched}',timeStart='{start}',timeEnd='{end}' WHERE stubCode='{code}'")
        return True
    except Exception as e:
        return False

# ============ SUBJECTS =============
# def getSubjects():
#     cur.execute("SELECT * FROM subjects")
#     return cur.fetchall()

#     def addTeacher(subjID, subjName):
#     try:
#         cur.execute(f"INSERT INTO subjects VALUES ('{subjID}', '{subjName}')")
#         return True
#     except Exception as e:
#         return False

# ============ RATING =============

def rateTeacher(teacherID, userID, rating, comment):
    cur.execute(f"INSERT INTO ratings(teacherID, studentID, rate, comment) VALUES('{teacherID}', '{userID}', {rating}, '{comment}')")
