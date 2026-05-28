
#import

import sqlite3







#function
connec = sqlite3.connect("Student Grade Tracker Database.db")  #connect to the database
helper = connec.cursor()                                       #create a cursor object to execute SQL commands



def print_grade_sorter(data_that_userneed=None):
    
    if data_that_userneed is None:
        sql_input = "SELECT * FROM Grade_tracker"
    else:
        sql_input = f"SELECT * FROM Grade_tracker ORDER BY {data_that_userneed} DESC;"
    
    helper.execute(sql_input)

    results = helper.fetchall()

    if data_that_userneed == "exam_name":
        print("student id     name   year level      subject                   score    grade        exam_name")
    elif data_that_userneed == "status":
        print("student id     name   year level      subject                   score    grade      status")
    elif data_that_userneed == "assignment_type":
        print("student id     name   year level      subject                   score    grade       assignment_type")
    else:
       print("student id     name   year level      subject                   score    grade")
    for data in results:

        normal_form =(f"{data[0]:<15}{data[1]:10}{data[2]:<10}{data[3]:<30}{data[7]:<10}{data[8]:<8}")

        if data_that_userneed == "exam_name":
            print(normal_form + f" | Exam: {data[4]}")
        elif data_that_userneed == "status":
            print(normal_form + f" | Status: {data[5]}")
        elif data_that_userneed == "assignment_type":
            print(normal_form + f" | Type: {data[6]}")
        else:
            print(normal_form)


def insert_new_grade(id, name, year, subject, e_name, status, type, score, grade)
      
    upload_to_sql = ("""
    INSERT INTO Grade_Tracker (student_id, student_name, year_level, subject, exam_name, status, assignment_type, score, grade)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """)
      
    helper.execute(upload_to_sql, (id, name, year, subject, e_name, status, type, score, grade))
    
    connec.commit



#main code

while True:
    try:
        read_or_write = input("\nDo you like read or write\n1.write\n2.read\n3.exit\n")
        if read_or_write in ["1","2","3"]:
            if read_or_write == "2":

                user_want = (input("\nWhat data would you like to see?\n1. Sort by [Student ID]\n2. Sort by [Student Name]\n3. Sort by [Year Level]\n4. Sort by [Subject]\n5. Sort by [Exam Name] (Extra Show)\n6. Sort by [Status] (Extra Show)\n7. Sort by [Assignment Type] (Extra Show)\n8. Sort by [Score]\n9. Sort by [Grade]\n10.Exit\nPlease enter the answer in number\n"))
                if user_want == "1":
                        print_grade_sorter()
                elif user_want == "2":
                        print_grade_sorter("student_name")
                elif user_want == "3":
                        print_grade_sorter("year_level")
                elif user_want == "4":
                        print_grade_sorter("subject")
                elif user_want == "5":
                        print_grade_sorter("exam_name")
                elif user_want == "6":
                        print_grade_sorter("status")
                elif user_want == "7":
                        print_grade_sorter("assignment_type")
                elif user_want == "8":
                        print_grade_sorter("score")
                elif user_want == "9":
                        print_grade_sorter("grade")
                elif user_want == "10":
                        continue
                else:
                        print("\nPlease enter a valid number") 

            if read_or_write == "3":
                break
        else:
                    print("\nPlease enter a valid number") 
        
    except ValueError:
           print("Please enter a valid number") 
