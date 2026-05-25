import sqlite3

connec = sqlite3.connect("Student Grade Tracker Database.db")  #connect to the database
helper = connec.cursor()                                       #create a cursor object to execute SQL commands

helper.execute("SELECT * FROM Grade_tracker")                  #execute the commands
data = helper.fetchall()                                       

for ans in data:
    print(ans)