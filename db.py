from config import config
import mysql.connector as mysql

db = mysql.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSOWRD, db=config.DB_DATABASE)
cur = db.cursor()

def getStudents():
    cur.execute("SELECT * FROM students")
    return cur.fetchall()

def getTeachers():
    cur.execute("SELECT * FROM teachers")
    return cur.fetchall()

def getSubjects():
    cur.execute("SELECT * FROM subjects")
    return cur.fetchall()