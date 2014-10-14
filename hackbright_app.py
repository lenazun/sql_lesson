import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" %(first_name, last_name)

def get_projects(title):
    query = """SELECT * FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
    Project: %s
    Description: %s
    Max Grade: %d """ % (row[1], row[2], row[3])

def add_project(title, description, max_grade):
    query = """INSERT INTO Projects (title, description, max_grade) VALUES (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Added project: %s, %s, %d" % (title, description, int(max_grade))

def get_grade(title, first_name, last_name):
    query = """SELECT * FROM GradesView WHERE project_title = ? AND first_name = ? AND last_name = ?"""
    DB.execute(query, (title, first_name, last_name))
    row = DB.fetchone()
    print "%s %s's grade on %s was %s" % (first_name, last_name, title, row[3])

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split(', ')
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            get_projects(*args)
        elif command == "add_project":
            add_project(*args)
        elif command == "get_grade":
            get_grade(*args)


    CONN.close()

if __name__ == "__main__":
    main()
